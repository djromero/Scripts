#!/bin/bash
#
# Create hard links for downloaded files (P2P) 
# in order to allow easy reorganization 
# without stop sharing them
#

# Directory to scan
ORIGIN="$@"
declare -a MEDIA_EXTENSIONS 

#### BEGIN CONFIGURATION ####

# Where to link files
TARGET="/path/to/media"

# Only files with these extensions will be linked
MEDIA_EXTENSIONS=(avi mpg4)

# recreate folders from origin in target? 0-No 1-Yes
CLONE_TREE=0

# 0-Do it 
# 1-Echo what will be done
# 2-Same as 1 but verbose
DEBUG=0

# ln path
LN_CMD="/bin/ln"

# overwrite existing files with -f
LN_CMD_FLAGS="-f"

#### END CONFIGURATION ####

SEP=""
PORIGIN=`dirname "$ORIGIN"`
declare -i CUT
CUT=`echo "$ORIGIN" | wc -c`
CUT=$CUT+1

preflight_check()
{
    if [ "$ORIGIN" == "" ]; then
        echo "Usage: $0 <folder-to-scan>"
        exit 1
    fi
    if [ ! -d "$ORIGIN" ]; then
        echo "Origin: opps, \"$ORIGIN\" should be a directory"
        exit 2
    fi
    if [ ! -d "$TARGET" ]; then
        echo "Target: opps, \"$TARGET\" should be a directory"
        exit 4
    fi
    if [ ! -x "$LN_CMD" ]; then
        echo "ln: opps, \"$LN_CMD\" should be executable"
        exit 8
    fi
}

check_extension()
{
    FPATH="$@" && shift
    BPATH=`basename "$FPATH"`
    for ext in ${MEDIA_EXTENSIONS[*]}
    do
        if [ $DEBUG -gt 1 ]; then
            echo $SEP echo \"$BPATH\" \| egrep \.$ext$
        fi
        # most people will use awk for this
        echo "$BPATH" | grep $ext > /dev/null
        if [ $? -eq 0 ];then
            return 0
        fi
    done
    return 1
}

do_HL()
{
    FPATH="$@" && shift
    if [ -f "$FPATH" ]; then
        if [ $DEBUG -gt 1 ]; then
            echo $SEP \"$FPATH\" is file
        fi
        check_extension "$FPATH"
        if [ $? -eq 0 ]; then
            FTARGET="$TARGET"
            if [ $CLONE_TREE -eq 1 ]; then
                FOLDER=`echo $FPATH | cut -b$CUT-`
                FTARGET=`dirname "$FTARGET/$FOLDER"`
                mkdir -p "$FTARGET"
            fi
            if [ $DEBUG -lt 1 ]; then
                $LN_CMD $LN_CMD_FLAGS "$FPATH" "$FTARGET"
            else
                echo $SEP $LN_CMD $LN_CMD_FLAGS \"$FPATH\" \"$FTARGET\"
            fi
        fi
    else if [ -d "$FPATH" ]; then
            if [ $DEBUG -gt 1 ]; then
                echo $SEP \"$FPATH\" is directory
            fi
            # 'find' will follow directories, no need to re-scan folders  here
            do_something_with_folder "$FPATH"
        fi
    fi
}

do_something_with_folder()
{
    return 0
}

do_scan()
{
    FPATH="$@" && shift
    echo $SEP Scanning \"$FPATH\"
    SEP="$SEP  .  . "
    find "$FPATH" | while read item
    do
        if [ "$item" != "$FPATH" ];then
            do_HL "$item"
        fi
    done
}

preflight_check
do_scan "$ORIGIN"
