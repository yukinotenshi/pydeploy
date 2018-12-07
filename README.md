# pydeploy
Automatically deploy git repositories

[![Build Status](https://travis-ci.com/yukinotenshi/pydeploy.svg?branch=master)](https://travis-ci.com/yukinotenshi/pydeploy)


## Background
I made this tool because I need something to
automatically deploy my web services on staging/testing
server. However, I don't really need it to be
robust like Jenkins. I only need a simple script
that just easily customizable, lightweight, and easy to configure.

## Installation
```
pip install pydeploycli
```

## Usage
1. Create a config file in JSON format like this
    ```
    {
        "pre_script": ["echo 1", "echo 2"],
        "post_script": ["python3 app.py"],
        "remote": "<remote>",
        "branch": "<branch>",
        "notifier": {
            "type": "<discord / slack>",
            "receiver": "<webhook>"
        }
    }
    ```
    pre_script are bash commands that are executed
    before pull.
    post_scripts are the same but executed after
    pull.
    You can ignore the notifier part if you don't
want to be notified. Save this config to file.

2. Clone your repository, move to your repository
directory. If your repository is private, you
can store your username & password first or use
ssh.

3. Execute pyDeploy in that directory
    ```
    pydeploy "path/to/config/file"
    ```

    Your webhook will be running on
    ```
    http://IP:9999/<endpoint>
    ```

    endpoint will be printed when you execute pydeploy
    you can also set your own endpoint by providing `--endpoint` option
4. Copy that webhook URL and put it on your
github webhook setting. Select the content type
to json.

5. Done! Now your server will automatically
pull and execute your predefined script.

## Issues? Changes?
Just open an issue/pull request. Thanks