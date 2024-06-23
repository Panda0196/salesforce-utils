# Salesforce Integration Utils
![Salesforce](img/salesforce.png)

## GET_NEW_ACCESS_TOKEN.PY

Python script to get new access token by using refresh token.

## REVOKE_TOKEN.PY

Python script to revoke refresh token.


### Why is the refresh token getting expired?

When the "Refresh token is valid until revoked" option is selected in the App OAuth policies, it is expected that the refresh token should remain valid until it is explicitly revoked. However, there are a few factors that could cause the refresh token to expire. Let's explore some possible reasons:

1. Multiple Approvals: If a user tries to log in more than five times, their oldest approval will be revoked. This can result in the refresh token becoming invalid.

2. Missing Scope? The refresh token may become invalid if the OAuth 2.0 scope does not include the "refresh_token" or "offline_access" scope. These scopes need to be explicitly included in the authorization request.

3. Too Many Access Grants? Salesforce allows only five access grants for a Connected App per user. If a user exceeds this limit, their oldest approval will be revoked, which can invalidate the refresh token.
