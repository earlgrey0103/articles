# 升级到Flask 0.11要注意哪些问题

Flask itself is changing like any software is changing over time. Most of the changes are the nice kind, the kind where you don’t have to change anything in your code to profit from a new release.

However every once in a while there are changes that do require some changes in your code or there are changes that make it possible for you to improve your own code quality by taking advantage of new features in Flask.

This section of the documentation enumerates all the changes in Flask from release to release and how you can change your code to have a painless updating experience.

If you want to use the easy_install command to upgrade your Flask installation, make sure to pass it the -U parameter:

$ easy_install -U Flask
Version 0.11
0.11 is an odd release in the Flask release cycle because it was supposed to be the 1.0 release. However because there was such a long lead time up to the release we decided to push out a 0.11 release first with some changes removed to make the transition easier. If you have been tracking the master branch which was 1.0 you might see some unexpected changes.

In case you did track the master branch you will notice that flask –app is removed now. You need to use the environment variable to specify an application.

Debugging
Flask 0.11 removed the debug_log_format attribute from Flask applications. Instead the new LOGGER_HANDLER_POLICY configuration can be used to disable the default log handlers and custom log handlers can be set up.

Error handling
The behavior of error handlers was changed. The precedence of handlers used to be based on the decoration/call order of errorhandler() and register_error_handler(), respectively. Now the inheritance hierarchy takes precedence and handlers for more specific exception classes are executed instead of more general ones. See Error handlers for specifics.

Trying to register a handler on an instance now raises ValueError.

Note
There used to be a logic error allowing you to register handlers only for exception instances. This was unintended and plain wrong, and therefore was replaced with the intended behavior of registering handlers only using exception classes and HTTP error codes.
Templating
The render_template_string() function has changed to autoescape template variables by default. This better matches the behavior of render_template().

Extension imports
Extension imports of the form flask.ext.foo are deprecated, you should use flask_foo.

The old form still works, but Flask will issue a flask.exthook.ExtDeprecationWarning for each extension you import the old way. We also provide a migration utility called flask-ext-migrate that is supposed to automatically rewrite your imports for this.
