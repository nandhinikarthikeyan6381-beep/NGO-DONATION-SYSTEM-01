document.addEventListener("DOMContentLoaded", () => {
    const amountInput = document.querySelector("#amount");
    const amountPreview = document.querySelector("#amountPreview");
    if (amountInput && amountPreview) {
        const update = () => amountPreview.textContent = "₹ " + (Number(amountInput.value || 0)).toLocaleString("en-IN");
        amountInput.addEventListener("input", update);
        update();
    }

    const donationType = document.querySelector("#donation_type");
    const productFields = document.querySelector("#productFields");
    const moneyFields = document.querySelector("#moneyFields");
    function toggleDonationFields() {
        if (!donationType) return;
        const money = donationType.value === "money";
        productFields?.classList.toggle("d-none", money);
        moneyFields?.classList.toggle("d-none", !money);
    }
    donationType?.addEventListener("change", toggleDonationFields);
    toggleDonationFields();

    document.querySelectorAll("[data-confirm]").forEach(btn => {
        btn.addEventListener("click", e => {
            if (!confirm(btn.dataset.confirm)) e.preventDefault();
        });
    });
});
