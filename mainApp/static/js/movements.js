let dataTable;
let dataTableIsInitialized = false;

const dataTableOptions = {
    columnDefs: [
        { className: "centered", targets: [0, 1, 2, 3, 4, 5, 6, 7]},
        { orderable: false, targets:[7]},
        { searchable: false, targets:[0, 7]}
    ]
};

const initDataTable = async() => {
    if(dataTableIsInitialized){
        dataTable.destroy();
    }

    await listMovements();

    dataTable = $('#datatable-movements').DataTable(dataTableOptions);
    dataTableIsInitialized = true;
};

const listMovements = async()=>{
    try{
        const response = await fetch("http://127.0.0.1:8000/movements-list-data/");
        const data = await response.json();

        let content = ``;
        data.movements.forEach((movements, index) =>{
            content += `
                <tr>
                    <td>${index+1}</td>
                    <td>${movements.date}</td>
                    <td>${movements.idOrigin_id}</td>
                    <td>${movements.idType_id}</td>
                    <td>${movements.idCategory_id}</td>
                    <td>${movements.idPayMethod_id}</td>
                    <td>${movements.amount}</td>
                    <td>${movements.observations}</td>
                </tr>
            `;
        });
        tableBody_movements.innerHTML = content;
    }catch (ex){
        alert(ex);
    }

};

window.addEventListener('load', async()=>{
    await initDataTable();
});