
# Authentication

While most of the endpoints exposed by the public registry allow authentication with a bearer token provided by the OAuth 2.0 flow, it is recommended to use the TRM token instead.

> **Warning**
Api and registry endpoints may not allow authentication with a bearer token at any time.

## Generating a TRM Token

TRM Tokens allow users to call any public registry endpoint, including APIs and registry.

To generate a new TRM Token, first [log into your account](https://trmregistry.com/profile) and visit the **Manage** section.

<p align="center">
  <img src="../_media/profile_dropdown.png" />
</p>

Navigate to the **API/Registry Tokens** section and press **Generate new token**.

> Each user can generate only one token for security reasons. You may revoke a token at any time.

Once the login is completed, you will be brought back to the manage page, and the token will appear in the list.

<p align="center">
  <img src="../_media/token_generation.png" />
</p>

At this point, **this is your only chance to copy the generated token**.

Press on the token generated to copy the value to your clipboard and store it in a safe place.

This token is linked to the user, has a validity of 10 years and gives access to all endpoints.

## API Header

In order to authenticate, the token generated in the step above must be provided in the Authorization header like this:

`Authorization`: `token <<YOUR_TOKEN>>`