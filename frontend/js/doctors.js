const API_URL = 'http://127.0.0.1:5000/api/doctors';

async function loadDoctors() {
    const response = await fetch(API_URL);
    const doctors = await response.json();

    const list = document.getElementById('doctors-list');
    list.innerHTML = '';

    doctors.forEach(d => {
        const li = document.createElement('li');
        li.textContent = `Номер: ${d.id}, ${d.name}, возраст: ${d.age}, пол: ${d.sex}`;
        list.appendChild(li);
    });
}

async function addDoctor() {
    const data = {
        name: document.getElementById('add_name').value,
        age: document.getElementById('add_age').value,
        sex: document.getElementById('add_sex').value
    };

    await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    loadDoctors();
}

async function updateDoctor() {
    const doctorId = document.getElementById('update_id').value;
    const data = {
        name: document.getElementById('update_name').value,
        age: document.getElementById('update_age').value,
        sex: document.getElementById('update_sex').value
    };

    await fetch(`${API_URL}/${doctorId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    loadDoctors();
}

async function deleteDoctor() {
    const doctorId = document.getElementById('delete_id').value;

    await fetch(`${API_URL}/${doctorId}`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' }
    });

    loadDoctors();
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('add-btn')
        .addEventListener('click', addDoctor);
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('update-btn')
        .addEventListener('click', updateDoctor);
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('delete-btn')
        .addEventListener('click', deleteDoctor);
});


document.addEventListener('DOMContentLoaded', loadDoctors);
