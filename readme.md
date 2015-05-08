Copyright &copy; 2015, [Brendan Doms](http://www.bdoms.com/)  
Licensed under the [MIT license](http://www.opensource.org/licenses/MIT)

# Slack

A dead simple Python interface to the Slack API.

This is primarily meant for use with [incoming webhooks](https://api.slack.com/incoming-webhooks).

## Setup

[Create an incoming webhook.](https://my.slack.com/services/new/incoming-webhook/)
The URL there is the value of the `url` argument you should pass when creating a client.
