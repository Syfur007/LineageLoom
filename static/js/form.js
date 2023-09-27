const form = document.querySelector("form"),
        nextBtn = form.querySelector(".nextBtn"),
        backBtn = form.querySelector(".backBtn"),
        allInput = form.querySelectorAll(".first input[required]");


nextBtn.addEventListener("click", (event) => {
    event.preventDefault(); // Prevent the form from being submitted

    // Check if all required fields are filled
    if (validateRequiredFields()) {
        form.classList.add('secActive');
    } else {
        alert("Please fill in all required fields before proceeding.");
    }
});

// Function to validate required fields
function validateRequiredFields() {
    let isValid = true;
    allInput.forEach((input) => {
        if (input.value.trim() === "") {
            isValid = false;
        }
    });
    return isValid;
}

backBtn.addEventListener("click", () => form.classList.remove('secActive'));


const districts = {
    Dhaka: ["Dhaka", "Gazipur", "Narayanganj", "Tangail", "Munshiganj", "Manikganj", "Rajbari", "Faridpur", "Kishoreganj", "Shariatpur", "Madaripur"],
    Chittagong: ["Chittagong", "Cox's Bazar", "Feni", "Khagrachari", "Rangamati", "Bandarban", "Chandpur", "Noakhali", "Lakshmipur", "Comilla"],
    Rajshahi: ["Rajshahi", "Bogra", "Pabna", "Sirajganj", "Naogaon", "Joypurhat", "Chapainawabganj", "Natore"],
    Khulna: ["Khulna", "Jessore", "Satkhira", "Bagerhat", "Chuadanga", "Kushtia", "Magura", "Meherpur", "Jhenaidah", "Narail"],
    Barishal: ["Barishal", "Bhola", "Patuakhali", "Pirojpur", "Jhalokati", "Barguna"],
    Sylhet: ["Sylhet", "Moulvibazar", "Habiganj", "Sunamganj"],
    Rangpur: ["Rangpur", "Dinajpur", "Thakurgaon", "Panchagarh", "Kurigram", "Nilphamari", "Lalmonirhat"],
    Mymensingh: ["Mymensingh", "Netrokona", "Jamalpur", "Sherpur"]
};

// Function to update the district dropdown based on the selected division
function updateDistricts() {
    const divisionSelect = document.getElementById("division");
    const districtSelect = document.getElementById("district");
    const selectedDivision = divisionSelect.value;

    // Clear previous options in the district dropdown
    districtSelect.innerHTML = "<option value=''>Select District</option>";

    // Populate the district dropdown with options based on the selected division
    if (selectedDivision !== "") {
        const divisionDistricts = districts[selectedDivision];
        for (const district of divisionDistricts) {
            const option = document.createElement("option");
            option.value = district;
            option.textContent = district;
            districtSelect.appendChild(option);
        }
    }
}