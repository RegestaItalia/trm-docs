# Authentication

While most endpoints in the TRM Public Registry support **OAuth 2.0 bearer tokens**, it is **recommended** to use a **TRM Token** for authentication — especially for automation and API usage.

> ⚠️ **Warning**  
> Use a TRM token for full compatibility.

---

## Generating a TRM Token

A **TRM Token** allows secure access to all TRM Public Registry endpoints, including REST APIs and registry operations.

### Steps to Generate a Token

1. [Log into your account](https://trmregistry.com/profile)
2. Go to the **Manage** section.

<p align="center">
  <img src="/_media/profile_dropdown.png" alt="Profile menu dropdown" />
</p>

3. Navigate to the **API/Registry Tokens** section and click **Generate new token**.

> ✅ Each user may generate **only one token** at a time for security reasons.  
> You can revoke and regenerate the token at any time.

Once the token is generated, it will appear in your token list.

<p align="center">
  <img src="/_media/token_generation.png" alt="TRM token generation screen" />
</p>

> ⚠️ **Important**  
> This is your **only chance** to copy the token. Make sure to save it securely. Copy is done by clicking on the generated token.

The generated token is:
- **User-specific**
- **Valid for 10 years**
- Grants access to **all public registry endpoints**

---

## Using the Token (API Header)

To authenticate API requests, include the TRM token in the `Authorization` header:

```
Authorization: token <<YOUR_TOKEN>>
```

Replace `<<YOUR_TOKEN>>` with the actual token string you copied during generation.

---

Keep your token secure and never share it in public repositories or exposed environments.
