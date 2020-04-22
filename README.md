this is a playground to understand how a webservice work.

```json
{
    "data": "mixed contiene la respuesta",
    "message":" descripcion de lo sucedido"
}
```

### list all devices
`GET /devices`

***response***
- `200 OK` on success

```json
[
    {
        "identifier" : "lampara",
        "name" : "lampara cuarto",
        "device_type": "switch",
        "controller_gateway": "192.168.0.2"
    },
    {
        "identifier":"samsung-tv",
        "name": "living tv",
        "device_type":"tv",
        "controller_gateway":"192.168.0.4"
    }
]
```

### registerin a new device
**definition**
`POST /devices`

- `"identifier":string` a globally unique identifier for this device
- `"name":string` a frienly name for the device.
- `"device_type":string` the typo of device understood by teh client.
- `"controller_gateway":string` el ip

if a device with the given identifier already exist, the existing device will be overwritten.

**response**
- `201 Created` on success

```json

{
     "identifier" : "lampara",
    "name" : "lampara cuarto",
    "device_type": "switch",
    "controller_gateway": "192.168.0.2"
}
```

## looup device details

`GET /device/<identifier>`

- `404 Not Found` if the device does not exist
- `202 OK` on success
```json

{
     "identifier" : "lampara",
    "name" : "lampara cuarto",
    "device_type": "switch",
    "controller_gateway": "192.168.0.2"
}
```

## delete a device
**definition**

`DELETE /device/<identifier>`

**response**

- `404 Not Fpund` if teh device does not exist
- `204  No content` no usefull data to return

# PyJWT

with the intention of using a web autentication service i choose JWT, in python there is a library call PyJWT. We just make use of it.

# MySql

for use of my sql we use mysql-connector which allow use to use MySql commands from python.


# TODO
* integrate everything.
