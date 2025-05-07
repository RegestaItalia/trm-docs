# Generate a TRM Token

TRM tokens are used by TRM clients to authenticate securely.

For a complete explanation on how TRM tokens work and how to use them, see the [Authentication Guide](/registry/public/authentication.md#generating-a-trm-token).

---

# Profile Management

## Manage Public Profile Data

Your TRM profile is **public**, meaning anyone can view your basic details.

To manage your profile:

1. [Log into your account](https://trmregistry.com/profile)
2. Go to the **Profile** section.

<p align="center">
  <img src="/_media/profile_dropdown.png" alt="Profile dropdown" />
</p>

3. Click the **Edit** button.

<p align="center">
  <img src="/_media/profile_edit_header.png" alt="Edit profile header" />
</p>

4. Modify your profile data as needed.

<p align="center">
  <img src="/_media/profile_edit.png" alt="Edit profile screen" />
</p>

> 💡 **Note**: Your email address is private by default. If you want to share it publicly, you can specify a separate **Contact Email**.

You can also update your **avatar**. To remove the current one, simply check the **Remove avatar** box.

When finished, click **Save** to apply the changes.

---

# Package Management

## Deleting a Package

You can delete a package only if you are authorized by its maintainers.

- Releases must be deleted **one version at a time**
- Once a version is deleted, it **cannot** be republished

To delete:

1. Open the package where you have edit access.

<p align="center">
  <img src="/_media/package_edit_header.png" alt="Edit package header" />
</p>

2. Click the **Delete** button to confirm.

> ⚠️ **Warning**: Deleting a package is **permanent and irreversible**.

---

## Editing a Package

You can edit a package only if you are an authorized maintainer.

- **Manifest values cannot be edited**. If changes are needed, [delete the package](#deleting-a-package) and publish a new version.

1. Open the package you wish to edit.

<p align="center">
  <img src="/_media/package_edit_header.png" alt="Edit package header" />
</p>

2. Click the **Edit** button.
3. After making your changes, click **Save**.

---

### Add Package Maintainers

If you have the proper permissions, you can add maintainers to a package.

1. Navigate to the **Maintainers** section.
2. Click the **Add** button in the top right of the table.

<p align="center">
  <img src="/_media/package_maintainers_section.png" alt="Maintainers section" />
</p>

3. Enter a unique, valid username (case-insensitive) for the new maintainer.

<p align="center">
  <img src="/_media/package_maintainers_add.png" alt="Add maintainer form" />
</p>

---

### Edit or Remove Maintainers

You can also manage maintainers if you have the required privileges.

1. In the **Maintainers** section, use the **trash bin** icon to remove a maintainer or the **pencil** icon to edit their details.

<p align="center">
  <img src="/_media/package_maintainers_section.png" alt="Maintainers controls" />
</p>

---

## Search for a Package

To search for packages:

1. Click the **Search** button next to your avatar (or the login icon if you're not signed in).

<p align="center">
  <img src="/_media/profile_dropdown.png" alt="Search entry point" />
</p>

2. Use the search bar to find:

- Public packages
- Private packages where you have view access (if logged in)
