# TRM Public Registry API Documentation


The public registry exposes REST APIs that may be used to perform actions programmatically.


Each of these endpoints requires [authentication](registry/public/authentication.md), request headers are documented in the appropriate section.


The public registry API base url is `https://www.trmregistry.com/api`.


This documentation lists all of the endpoints available, how requests should be made, responses interpreted, and errors handled.


> Some error codes might not be documented and should be handled as generic errors.


## /updateUser


Allows the currently authenticated user to edit one or more of its own properties.


> If a property has no value (or an invalid value), no changes will be applied to that property.


- Method `POST`
- Content type `multipart/form-data`
- Request body
- contactEmail - `string`

    User contact email

    - website - `string`

    User website link

    - github - `string`

    User Github profile link

    - linkedin - `string`

    User Linkedin profile link

    - sapblog - `string`

    User SAP Blog profile link

    - removeAvatar - `boolean`

    Remove profile avatar

        - avatar - `file`

    User profile avatar.

    Has no effect if removeAvatar is set to `true`.
- Response type `application/json`
- Response

    - Code `304`

        No changes applied.

    - Code `200`

        Returns updated user data.


## /updatePackage


Update package data.


- Method `POST`
- Content type `application/json`
- Request body
    - readme - `string`

        Valid markdown.

    - packageMaintainers - `array`

        - Object

            ```
            {
                username: string,
                canEditReleases: boolean,
                canEditPackage: boolean,
                canEditUsers: boolean
            }
            ```
        Valid username must be provided for each object.

- Response type `application/json`
- Response

    - Code `200`

        Package updated.

## /revokeToken


Revoke a TRM token.


The authenticated user **must** be the owner of the token to revoke.


- Method `POST`
- Content type `application/json`
- Request body

    - tokenId - **required** - `string`

        ID of the token to revoke.

- Response type `application/json`
- Response
    
    - Code `200`
        
        Token has been revoked.
   

## /deleteUser


Delete the currently authenticated user.


> **Warning**
This has immediate effect and will delete the account forever!
Use with caution.


- Method `POST`
- Response type `application/json`
- Response

    - Code `200`

        User has been deleted.