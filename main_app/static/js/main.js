const dateEl = document.getElementById('id_date');
M.Datepicker.init(dateEl, {
    format: 'yyyy-mm-dd',
    defaultDate: new Date(),
    setDefaultDate: true,
    autoClose: true
});

const selectEl = document.getElementById('id_meal');
M.FormSelect.init(selectEl);

const statusEl = document.getElementById('id_status');
M.FormSelect.init(statusEl)