# Video-Downloader

Тhis code is aimed at the possibility of downloading videos from the Internet spaces without having to use paid services that are offered by a number of sites.
Applies references to some additional settings to enable the use of this code.

№ Here's a detailed step-by-step guide on how to add ffmpeg to your system's PATH on Windows:
Step 1: Download and Extract ffmpeg

    Download ffmpeg:
        Go to the official FFmpeg download page. [(https://ffmpeg.org/download.html)](url)
        Choose the Windows version and download the ZIP file.

    Extract the ZIP file:
        Locate the downloaded ZIP file (usually in your Downloads folder).
        Right-click on the ZIP file and select "Extract All..." or use a tool like WinRAR or 7-Zip to extract the contents.
        Extract it to a folder, for example, C:\ffmpeg. This folder will now contain several subfolders, including a bin folder.

Step 2: Access System Properties

    Right-click on "This PC" or "My Computer":
        On your desktop or in File Explorer, locate the "This PC" or "My Computer" icon.
        Right-click on it and choose "Properties" from the context menu.

    Open Advanced System Settings:
        In the System window that opens, find and click on the "Advanced system settings" link on the left side of the window.

Step 3: Edit Environment Variables

    Open Environment Variables:
        In the "System Properties" window, you'll see several tabs. Click on the "Advanced" tab (if it's not already selected).
        Click on the "Environment Variables..." button near the bottom of this window.

    Locate the Path Variable:
        In the "Environment Variables" window, you'll see two sections: "User variables" (specific to your user account) and "System variables" (for all users on the computer).
        Scroll down in the "System variables" section and find the variable named Path.

    Edit the Path Variable:
        Select the Path variable by clicking on it, then click the "Edit..." button.

Step 4: Add ffmpeg to the Path

    Add New Path:
        In the "Edit Environment Variable" window that opens, you'll see a list of paths already in the Path variable.
        Click the "New" button on the right side.

    Enter the ffmpeg bin Folder Path:
        Type or paste the full path to the bin folder inside the ffmpeg directory you extracted earlier. For example, if you extracted ffmpeg to C:\ffmpeg, you should add:

        makefile

        C:\ffmpeg\bin

        Press Enter after typing the path.

    Save Your Changes:
        After adding the new path, click "OK" to close the "Edit Environment Variable" window.
        Click "OK" again in the "Environment Variables" window.
        Finally, click "OK" in the "System Properties" window to apply the changes.

Step 5: Verify the Installation

    Open a Command Prompt:
        Press Win + R, type cmd, and press Enter to open a Command Prompt.

    Check if ffmpeg is Recognized:
        In the Command Prompt, type:

        bash

        ffmpeg -version

        If ffmpeg is correctly added to the PATH, you should see the version information of ffmpeg displayed in the Command Prompt.

Step 6: Restart PyCharm

    If PyCharm was open during this process, close and reopen it to ensure it recognizes the updated PATH environment variable.

After following these steps, ffmpeg should be available for any program, including yt-dlp, that requires it for processing videos.

Good luck!
