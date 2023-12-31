# TRM Registry Endpoints Documentation

All of the following endpoints should be reached from the same base URL.

> The implementation of the endpoint is up to the maintainer of the registry, and the descriptions provided below are generic.

> Errors, unless specified, are handled as generic by the clients.

## /ping

This is the first request made by the client in order to

- Check the registry is available
- Get registry config data

- Method `GET`
- Response type `application/json`
- Response
    - Code `200`

        Returns [Ping](/registry/private/api/types/responses.md#ping).

## /whoami

The client makes a request to this endpoint each time the logged user data is required.

> This endpoint might not be implemented depending on the authentication strategy applied by the registry.

- Method `GET`
- Response type `application/json`
- Response
    - Code `200`
    
        Returns [WhoAmI](/registry/private/api/types/responses.md#whoami).

## /auth

The client makes a request to this endpoint each time a login operation is required.

> This endpoint might not be implemented depending on the authentication strategy applied by the registry.

- Method `POST`
- Content type `application/json`
- Request body [OAuth2Body](/registry/private/api/types/requests.md#oauth2body).
- Response type `application/json`
- Response
    - Code `200`

        Returns [AuthOAuth2](/registry/private/api/types/responses.md#authoauth2).

## /view

The client makes a request to this endpoint each time a package data is requested.

- Method `GET`
- Content type `application/json`
- Request query
    - name - **required** - `string`
        
        Full package name.
        
    - version - `string`
    
        Package version.

- Response type `application/json`
- Response
    - Code `400`

        Package not found.
        
        Returns [View](/registry/private/api/types/responses.md#view), where all properties should be ignored except for `userAuthorizations`, that shall provide authorization data on the package with the requested values.

    - Code `404`

        Package not found and, with the requested data, will never be available (blacklisted package name/version, package name similar to others...).
        
        Returns [View](/registry/private/api/types/responses.md#view), where all properties should be ignored except for `userAuthorizations`, that shall provide authorization data on the package with the requested values.

    - Code `200`
        
        Returns [View](/registry/private/api/types/responses.md#view).

## /releases

The client makes a request to this endpoint each time a package list of releases is required.

- Method `GET`
- Content type `application/json`
- Request query
    - name - **required** - `string`
        
        Full package name.
        
    - version - `string`
    
        Package specific version or range.

- Response type `application/json`
- Response
    - Code `200`
    
        Returns an array of [Release](/registry/private/api/types/responses.md#release).

## /publish

The client makes requests to this endpoint whenever a package needs to be published.

- Method `GET`
- Content type `multipart/form-data`
- Request body
    - artifact - **required** - `file`
    
        Package in .trm format, build by the TRM client.
    
    - readme - `string`
    
        Package readme (markdown).

- Response type `application/json`
- Response
    - Code `200`

        Package has been published.

## /unpublish

The client makes requests to this endpoint whenever a package needs to be published.

- Method `POST`
- Content type `application/json`
- Request body
    - package - **required** - `string`

        Package full name. (If scoped `@<<SCOPE>>/<<PACKAGE_NAME>>`).
    
    - version - **required** - `string`
    
        Version to unpublish.

        Only specific versions are allowed.

- Response type `application/json`
- Response
    - Code `200`

        Package has been unpublished.

## /install

The client makes a request to this endpoint each time a package needs to be installed.

- Method `GET`
- Content type `application/json`
- Request query
    - name - **required** - `string`
    
        Full package name.
    
    - version - `string`
        
        Package version.

- Response type `application/octet-stream`
- Response
    - Code `200`
    
        Returns the build package in .trm format.