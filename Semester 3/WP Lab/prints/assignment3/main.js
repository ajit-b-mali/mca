function validateForm() {
    const patientId = document.getElementById("patientId").value.trim();
    const patientName = document.getElementById("patientName").value.trim();
    const address = document.getElementById("address").value.trim();
    const city = document.getElementById("city").value.trim();
    const contact = document.getElementById("contact").value.trim();
    const dob = document.getElementById("dob").value;

    let errors = [];

    // Validation rules
    if (patientId === "") errors.push("Patient ID is required.");
    if (patientName === "" || !/^[A-Za-z ]+$/.test(patientName))
        errors.push("Valid Patient Name is required.");
    if (address === "") errors.push("Address is required.");
    if (city === "" || !/^[A-Za-z ]+$/.test(city))
        errors.push("Valid City name is required.");
    if (!/^\d{10}$/.test(contact))
        errors.push("Contact Number must be 10 digits.");
    if (!dob) {
        errors.push("Date of Birth is required.");
    } else {
        const dobDate = new Date(dob);
        const today = new Date();
        if (dobDate >= today)
            errors.push("Date of Birth must be in the past.");
    }

    // Show errors or submit
    const errorDiv = document.getElementById("errorMessages");
    if (errors.length > 0) {
        errorDiv.innerHTML = errors.join("<br>");
        return false;
    } else {
        errorDiv.innerHTML = "";

        return true;
    }
}