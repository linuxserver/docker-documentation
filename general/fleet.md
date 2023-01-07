---
description: >-
  Fleet is a web-based image management tool for organisations who ship a large
  list of Docker images.
---

# Fleet

## How Fleet works

Fleet stores a snapshot of Docker Images in its own database, consisting of metadata deemed most pertinent to both the users of the images, and the repository owner. It will synchronize with Docker Hub over a set interval in order to update its stored data.

It then displays this snapshot data on its own status page as a useful list, containing links to each repository and image owned by the repository owner. Each image also contains a status which is managed by the repository owner, who can define images as either _Stable_ or _Unstable_. This is designed to quickly help users know when an image is undergoing a state of instability which is known by the owner.

### Why a snapshot?

In short, Docker Hub's API is very slow. It would not be a good long-term solution to just proxy the responses from Docker Hub and translate the data into something considered useful by downstream clients. By caching the image information in its own database, Fleet is able to more efficiently return the status data for each image and repository. In doing so, it is also able to provide more concise data, such as image versions, as part of the primary response, rather than requiring users to make a separate call.

As an example comparison between obtaining all image name, pull and version information for all LinuxServer images from Docker Hub, and then obtaining that same data via Fleet's API:

| API | Time \(ms\) |
| :--- | :--- |
| Docker Hub \(multiple calls\) | 52000ms |
| Fleet | 50ms |

## Capabilities

Fleet has the ability to display images with a particular state, which provides contextual information to visitors of the application's main page.

### Hidden

If an image is hidden, it will not be displayed as part of the main list, nor will it be returned as part of any API calls. This also means that the pull count of a hidden image is not included.

### Unstable

Marks an image as having issues known by the maintainer. A useful state to assign to an image if the latest build \(or builds\) are causing downstream breakages. This may also be useful if an upstream dependency or application is causing breakages in the image directly.

### Deprecated

If the maintainer of the image, or upstream application no longer wishes to provide support, or if the image has reached its end-of-life \(or has been superseded by another\), marking an image as deprecated will ensure users are made aware that no further updates will be supplied, and should stop using it. Deprecation notices are also provided to give context.

## API

Fleet exposes a single API endpoint which can be used to obtain image list and pull count information for all relevant images maintained by the repository

{% api-method method="get" host="https://fleet.linuxserver.io" path="/api/v1/images" %}
{% api-method-summary %}
Get All Repositories and Images
{% endapi-method-summary %}

{% api-method-description %}
Returns all synchronized images.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
All synchronized repositories and images returned.
{% endapi-method-response-example-description %}

```javascript
{
    "status": "OK",
    "data" {
        "totalPullCount": 1862494227,
        "repositories": {
            "lsiobase": [
                {
                    "name": "alpine",
                    "pullCount": 4275970,
                    "version": "3.6",
                    "stable": true
                },
                {
                    "name": "alpine.arm64",
                    "pullCount": 66234,
                    "version": "edge",
                    "stable": true
                },
                ...
            ],
            "linuxserver": [
                {
                    "name": "airsonic",
                    "pullCount": 4608329,
                    "version": "v10.2.1",
                    "stable": true
                },
                {
                    "name": "apache",
                    "pullCount": 3011699,
                    "version": "latest",
                    "stable": true
                },
                ...
            ]
            ...
        }
    }
}
```

{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}

{% hint style="info" %}
Any repositories not synchronized with Docker Hub \(e.g. staging or metadata repositories\) will not be returned as part of the API. This also applies to images which the repository owner does not wish to be part of the primary image list.
{% endhint %}

## Running Fleet

{% hint style="warning" %}
Fleet is a Java application and requires at least JRE 11.
{% endhint %}

Grab the latest Fleet release from [GitHub](https://github.com/linuxserver/fleet/releases).

### SQL

Fleet stores its data in a MariaDB database which you need to provide. In order for the application to manage its tables and procedures, the user you provide it needs to have the relevant `GRANT` permissions to the fleet database. The following script should be sufficient to get the initial database set up.

```sql
CREATE SCHEMA `fleet`;
CREATE USER 'fleet_user' IDENTIFIED BY 'supersecretpassword';
GRANT ALL ON `fleet`.* TO 'fleet_user';
```

The username and password that you define must then be provided as part of Fleet's configuration.

### Configuration File

All primary configuration for Fleet at runtime is loaded in via a `fleet.properties` file. This can be located anywhere on the file system, and is loaded in via a Runtime argument:

```shell
# Runtime
fleet.app.port=8080

# Database Connectivity
fleet.database.driver=org.mariadb.jdbc.Driver
fleet.database.url=jdbc:mariadb://<IP_OR_URL>:3306/fleet
fleet.database.username=<fleet_sql_user>
fleet.database.password=<fleet_sql_password>

# Password security
fleet.admin.secret=<a_random_string>
```

All configuration can be loaded either via the config file, via JVM arguments, or via the system environment. Fleet will first look in the configuration file, then JVM runtime, and finally in the system environment. It will load the first value it finds, which can be useful when needing to override specific properties.

{% hint style="info" %}
If you place a property in the system environment, ensure that the property uses underscores rather than periods. This is due to a limitation in BASH environments where exported variables must not contain this character. E.g. `fleet.app.port=8080` becomes `export fleet_app_port=8080`
{% endhint %}

| Property Name | Purpose |
| :--- | :--- |
| `fleet.app.port` | The port which the application will be running under. |
| `fleet.admin.secret` | A string used as part of the password key derivation process. This secret is prepended to the raw password before its key is derived, providing further pseudo-randomness to hashed passwords. **Once set, this must not be changed!** It is vital to remain the same, as it will be used during the password verification step. If Fleet is restarted with this removed or set differently, the password verification process will fail because previously hashed passwords will have been derived with the old secret. |
| `fleet.database.driver` | The driver to use for connections to Fleet's database. This should be `org.mariadb.jdbc.Driver` |
| `fleet.database.url` | The full JDBC connection string to the database. |
| `fleet.database.username` | The username of the SQL user which will be managing the data in the Fleet database. **This should have full GRANT access** to the fleet database as it also manages any database migrations. |
| `fleet.database.password` | The password for the SQL user |

### Runtime Arguments

As well as the base configuration file, Fleet also supports some runtime arguments by means of the `-D` flag. These can be used to direct Fleet to behave in a specific way at runtime.

{% hint style="info" %}
Unlike the properties defined above, these properties are only accessed via the JVM arguments \(`-D`\).
{% endhint %}

| Runtime Argument | Purpose |
| :--- | :--- |
| `fleet.config.base` | The absolute path of the configuration file. |
| `fleet.show.passwords` | Tells fleet to show passwords in plain text in its logs. **Not recommended**. |
| `fleet.nuke.database` | **Be very careful.** This will tell Fleet to completely wipe and rebuild its database. This can be useful if the owner deems the database to be too far out of synchronisation with Docker Hub, or if images have since been removed but are still showing in Fleet. |
| `fleet.skip.sync.on.startup` | By default, Fleet will run a synchronisation process when it first starts up. Setting this flag will tell it to skip the first run. The next synchronisation will be at the set interval. |

### Default User

When starting Fleet for the first time it will create a default user in order for you to log in and manage the repositories/images synchronised by the application. The default username and password are:

**Username**: admin

**Password**: admin

{% hint style="warning" %}
You should change the default password for this user as soon as possible! This can be done via the `Admin` -&gt; `Users` menu options.
{% endhint %}
