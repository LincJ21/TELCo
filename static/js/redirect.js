function redirectToSSO() {
    var ssoProvider = document.getElementById("sso_provider").value;
    var url = "";

    if (ssoProvider === "gmail") {
        url = "/auth/google";
    } else if (ssoProvider === "facebook") {
        url = "/auth/facebook";
    }

    if (url) {
        window.location.href = url;
    } else {
        alert("Por favor, seleccione un proveedor de SSO.");
    }
}
