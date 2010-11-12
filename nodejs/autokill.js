/* 
 * node-autokill
 *
 * Kill itself when a change is detected in any of the watched files.
 *
 * AutoKill.watch(directory, pattern, delegate);
 * -- directory: absolute path to directory being watched
 * -- pattern: regular expression to match against file names
 * -- delegate: object to ask permission before exiting
 *
 * Example:
 *
 * require('autokill').watch(__dirname, /.(js|html)$/, {
 *     canExit : function(filename) {
 *         // decide to exit or not 
 *         return true;
 *     }
 * });
 *
 */

var fs = require('fs');
var sys = require('sys');
var path = require('path');

var AutoKill = exports;

AutoKill.options = {
    quiet : true,    /* say nothing at all */
    verbose : false, /* be extra verbose */
    interval : 100   /* watch files each # milliseconds  */
}

AutoKill.watch = function(directory, pattern, delegate) {
    fs.readdir(directory, function(err, files) {
        files.forEach(function(filename) {
            filename = path.join(directory, filename);
            _info("Considering " + filename);
            fs.stat(filename, function(err, stat) {
                if (err || !stat) {
                    _err(err);
                } else {
                    if (stat.isDirectory()) {
                        _info("...watching subdirectory " + filename);
                        AutoKill.watch(filename, pattern, delegate);
                    } else {
                        if (filename.match(pattern)) {
                            _log("+ Watching " + filename);
                            fs.watchFile(filename, {interval:AutoKill.options.interval}, function(curr, prev) {
                                /* check modification time */
                                if (curr.mtime.toString() != prev.mtime.toString()) {
                                    /* asks the delegate before exiting */
                                    if (delegate && typeof delegate.canExit == 'function' && delegate.canExit()) {
                                        _log("Killing myself (" + filename + ")");
                                        process.exit();
                                    }
                                }
                            })
                        }
                    } 
                }
            })
        })
    })
}

function _log(message) {
    if (AutoKill.options.quiet) return;
    console.log(message);
}

function _err(message) {
    if (AutoKill.options.quiet) return;
    console.error(message);
}

function _info(message) {
    if (AutoKill.options.quiet) return;
    if (!AutoKill.options.verbose) return;
    console.info(message);
}
