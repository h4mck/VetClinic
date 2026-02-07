const API_URL = 'http://127.0.0.1:5000/api/appointments';

async function loadAppointments() {
    const response = await fetch(API_URL);
    const appointments = await response.json();

    const list = document.getElementById('appointments-list');
    list.innerHTML = '';

    appointments.forEach(a => {
        const li = document.createElement('li');
        li.textContent = `Номер: ${a.id}, Номер пациента: ${a.patient_id}, Номер доктора: ${a.doctor_id}, ${a.date}, причина: ${a.reason}`;
        list.appendChild(li);
    });
}

async function addAppointment() {
    const data = {
        patient: document.getElementById('add_patient').value,
        doctor: document.getElementById('add_doctor').value,
        date: document.getElementById('add_date').value,
        reason: document.getElementById('add_reason').value,
    };

    await fetch(API_URL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    loadAppointments();
}

async function updateAppointment() {
    const appointmentId = document.getElementById('update_id').value;
    const data = {
        patient: document.getElementById('update_patient').value,
        doctor: document.getElementById('update_doctor').value,
        date: document.getElementById('update_date').value,
        reason: document.getElementById('update_reason').value
    };

    await fetch(`${API_URL}/${appointmentId}`, {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(data)
    });

    loadAppointments();
}

async function deleteAppointment() {
    const appointmentId = document.getElementById('delete_id').value;

    await fetch(`${API_URL}/${appointmentId}`, {
        method: 'DELETE',
        headers: { 'Content-Type': 'application/json' }
    });

    loadAppointments();
}

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('add-btn')
        .addEventListener('click', addAppointment);
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('update-btn')
        .addEventListener('click', updateAppointment);
});

document.addEventListener('DOMContentLoaded', function() {
    document.getElementById('delete-btn')
        .addEventListener('click', deleteAppointment);
});


document.addEventListener('DOMContentLoaded', loadAppointments);
