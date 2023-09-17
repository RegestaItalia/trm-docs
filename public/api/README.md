# TRM Public Registry API Documentation

The public registry exposes REST APIs that may be used to perform actions programmatically.

Each of these endpoints requires authentication.

## /updateUser
- Method `POST`
- Content type `multipart/form-data`
- Body
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

## /updateReadme
- Method `POST`
- Content type `application/json`
- Query parameters
    - package - **required** - `string`
    
        Package name.
- Body
    - rawText - `string`
    
        Package readme.
