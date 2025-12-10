# API Documentation

This document provides instructions on how to use the analytics and logging endpoints.

## Log User Event

This endpoint is used to log user interaction events for analytics.

**Endpoint:** `POST https://standard.trysixth.com/log_user_event`

**Request Body:**

```json
{
  "anonymous_user_id": "string",
  "event": "string"
}
```

**Parameters:**

*   `anonymous_user_id` (string, required): A unique identifier for the anonymous user. This is the user id/ apikey we saved
*   `event` (string, required): A description of the event that occurred (e.g., "user_clicked_save_button").

**Example Usage:**

```bash
curl -X POST "https://standard.trysixth.com/log_user_event" \
-H "Content-Type: application/json" \
-d '{
  "anonymous_user_id": "user_anon_12345",
  "event": "Opened the new feature modal"
}'
```

## Update Analytics Summary

This endpoint is used to update the daily analytics summary with aggregate data. You can send one or more counters to be incremented.

**Endpoint:** `POST https://standard.trysixth.com/update_analytics_summary`

**Request Body:**

```json
{
  "summary_updates": {
    "total_number_of_users_who_installed": 1,
    "total_number_of_users_who_clicked_on_chat": 1
  }
}
```

**Parameters:**

*   `summary_updates` (object, required): A dictionary where keys are the names of the counters to be incremented and values are the amount to increment by (usually 1).

**Events we will be using and when we will be using them:**

*   `total_number_of_users_who_installed` // use this event in the payload immediately they install the vscode endpoint
*   `total_number_of_users_who_passed_onboarding` // silently use this event immediately they click on the get started for free button in the welcomscreen
*   `total_number_of_users_who_registered` // use this event when we get /auth uri callback in the uri handler
*   `total_number_of_users_who_hit_free_trial_limit_for_the_day` //use the event when the user hits their free trial
*   `total_number_of_users_who_went_to_checkout` // use this event when user click on the upgrade button in both the paywall and the accounts tab
**Example Usage:**

```bash
curl -X POST "https://standard.trysixth.com/update_analytics_summary" \
-H "Content-Type: application/json" \
-d '{
  "summary_updates": {
    "total_number_of_users_who_went_to_checkout": 1
  }
}'