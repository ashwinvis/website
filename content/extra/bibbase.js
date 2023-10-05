// Function to inject the script's result into the target div
function injectScriptResult(result) {
    var targetDiv = document.getElementById('bibbaseTarget');
    targetDiv.innerHTML = result;
}

// Function to load the remote script and execute it
function loadRemoteScript(url) {
    var script = document.createElement('script');
    script.src = 'https://bibbase.org/show?bib=https%3A%2F%2Fapi.zotero.org%2Fusers%2F3909932%2Fcollections%2F4TSHE4HW%2Fitems%3Fkey%3DWiDPhsXd8GaIS4rnJu4WaDqJ%26format%3Dbibtex%26limit%3D100&jsonp=1';
    // script.defer = true;
    script.async = true;

    // After the script is loaded, inject its result into the target div
    script.onload = function () {
        var result = document.write.toString(); // Capture the output of document.write
        injectScriptResult(result);
    };

    document.head.appendChild(script);
}

// Call the function with the URL of the remote script you want to execute
loadRemoteScript();
