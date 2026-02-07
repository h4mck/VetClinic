const API_URL = 'http://127.0.0.1:5000/api/patients';

async function loadPatients() {
    const response = await fetch(API_URL);
    const patients = await response.json();

    const list = document.getElementById('patients-list');
    list.innerHTML = '';

    patients.forEach(p => {
        const li = document.createElement('li');
        li.textContent = `Номер: ${p.id}, ${p.name}, хозяин: ${p.owner}, медицинская карточка: ${p.medical_card_id}`;
        list.appendChild(li);
    });
}

async function addPatient() {
    const data = {
        name: document.getElementById('add_name').value,
        owner: document.getElementById('add_owner').value
    };

    await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    loadPatients();
}

async function updatePatient() {
    const patientId = document.getElementById('update_id').value;
    const data = {
        name: document.getElementById('update_name').value,
        owner: document.getElementById('update_owner').value
    };

    await fetch(`${API_URL}/${patientId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    loadPatients();
}

async function deletePatient() {
    const patientId = document.getElementById('delete_id').value;

    await fetch(`${API_URL}/${patientId}`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' }
    });

    loadPatients();
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('add-btn')
        .addEventListener('click', addPatient);
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('update-btn')
        .addEventListener('click', updatePatient);
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('delete-btn')
        .addEventListener('click', deletePatient);
});

document.addEventListener('DOMContentLoaded', loadPatients);
