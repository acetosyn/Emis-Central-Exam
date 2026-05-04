/*
  EMIS Central Exam - Admin Login Modal
*/

(function ($) {
    "use strict";

    function resetAdminLoginModal() {
        var adminLoginButton = $("#adminLoginButton");
        var adminPasswordInput = $("#admin_password");
        var adminPasswordToggle = $("#adminPasswordToggle");

        adminLoginButton.removeClass("is-loading");
        adminLoginButton.prop("disabled", false);

        adminPasswordInput.prop("readonly", false);
        adminPasswordInput.val("");
        adminPasswordInput.attr("type", "password");

        adminPasswordToggle.prop("disabled", false);
        adminPasswordToggle.html('<i class="fa fa-eye"></i>');
        adminPasswordToggle.attr("aria-label", "Show password");

        adminLoginButton.find(".admin-login-btn-text").text("Login to Admin Console");
    }

    function handleBackButtonRestore() {
        var adminLoginModal = $("#adminLoginModal");
        var hasAdminError = $("[data-admin-error='true']").length > 0;

        resetAdminLoginModal();

        if (hasAdminError) {
            adminLoginModal.modal("show");
        } else {
            adminLoginModal.modal("hide");
        }
    }

    /*
      Fix browser back button/cache issue.
      When user returns using browser back button, reset the modal state.
    */
    window.addEventListener("pageshow", function () {
        handleBackButtonRestore();
    });

    $(document).ready(function () {
        var adminLoginModal = $("#adminLoginModal");
        var adminLoginForm = $("#adminLoginForm");
        var adminPasswordInput = $("#admin_password");
        var adminPasswordToggle = $("#adminPasswordToggle");
        var adminLoginButton = $("#adminLoginButton");

        /*
          Re-open modal automatically when Flask returns an admin error.
        */
        if ($("[data-admin-error='true']").length > 0) {
            adminLoginModal.modal("show");
        }

        /*
          Password show/hide toggle.
        */
        adminPasswordToggle.on("click", function () {
            var inputType = adminPasswordInput.attr("type");

            if (inputType === "password") {
                adminPasswordInput.attr("type", "text");
                adminPasswordToggle.html('<i class="fa fa-eye-slash"></i>');
                adminPasswordToggle.attr("aria-label", "Hide password");
            } else {
                adminPasswordInput.attr("type", "password");
                adminPasswordToggle.html('<i class="fa fa-eye"></i>');
                adminPasswordToggle.attr("aria-label", "Show password");
            }
        });

        /*
          Show visible orbit/swirl loader when Login to Admin Console is clicked.
        */
        adminLoginForm.on("submit", function () {
            if (!adminPasswordInput.val().trim()) {
                return false;
            }

            adminLoginButton.addClass("is-loading");
            adminLoginButton.prop("disabled", true);

            adminPasswordInput.prop("readonly", true);
            adminPasswordToggle.prop("disabled", true);

            adminLoginButton.find(".admin-login-btn-text").text("Verifying Access...");
        });

        /*
          Reset modal fields when closed manually.
        */
        adminLoginModal.on("hidden.bs.modal", function () {
            resetAdminLoginModal();
        });
    });

})(jQuery);