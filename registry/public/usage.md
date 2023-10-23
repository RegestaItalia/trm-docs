# Generate a TRM Token

TRM Tokens are used by TRM Clients to authenticate.

Full explaination of TRM Tokens and how to use them is [here](/registry/public/authentication.md#generating-a-trm-token).

# Profile

## Manage public data

Your profile is public, and anyone can see its data.

To manage your profile, first [log into your account](https://trmregistry.com/profile) and visit the **Profile** section.

<p align="center">
  <img src="../_media/profile_dropdown.png" />
</p>

Next, press on the **Edit** button.

<p align="center">
  <img src="../_media/profile_edit_header.png" />
</p>

Now, you should be able to edit your profile data.

<p align="center">
  <img src="../_media/profile_edit.png" />
</p>

> The email is only visible to you. You can set a "Contact Email" if you want to share it publicly.

You can also edit your **avatar**; if you wish to remove your existing avatar, simply press on the "Remove avatar" checkbox.

When you're done editing, press the **Save** button to make the changes permanent.

# Packages

##  Publishing a package

Packages can only be published by using the registry APIs.

## Delete a package

Packages can be deleted if you are authorized by its maintainers.

Releases can be deleted **one at the time**, once a version is deleted, it cannot be republished.

First, open a package where you have edit privileges.

<p align="center">
  <img src="../_media/package_edit_header.png" />
</p>

Next, press on **Delete** to confirm the action.

> Warning
Deleting a package is a permanent and non-reversible action!

## Edit a package

Packages can be edited if you are authorized by their maintainers.

Manifest values cannot be changed; [delete the package](#delete-a-package) and republish a newer version with a different manifest instead.

First, open a package where you have edit privileges.

<p align="center">
  <img src="../_media/package_edit_header.png" />
</p>

Next, press on **Edit**.

When you're done editing, press the **Save** button to make the changes permanent.

### Add package maintainers

If you have edit maintainers privileges on a package, you can add maintainers.

Head over to the **Maintainers** section and press on the **Add** button on the top right of the table.

<p align="center">
  <img src="../_media/package_maintainers_section.png" />
</p>

The new maintainer username **must** be unique (in the package context), it's case insensitive and **must** be a valid username.

<p align="center">
  <img src="../_media/package_maintainers_add.png" />
</p>

### Edit package maintainers

If you have edit maintainers privileges on a package, you can edit and remove maintainers.

Head over to the **Maintainers** section and press on the trash bin button to **Delete** or the pencil button to **Edit**, next to the maintainer username.

<p align="center">
  <img src="../_media/package_maintainers_section.png" />
</p>

## Search a package

You can search for packages available on the registry.

Next to your profile avatar (or the login icon, if not logged in), press on the **Search** button.

<p align="center">
  <img src="../_media/profile_dropdown.png" />
</p>

This will open the search bar.

Public packages can be found with the search bar, as well as private packages where you have view access (if logged in).