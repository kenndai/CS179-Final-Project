
//makes the grid boxes for buffer and main grid zones
window.onload = function makeGrid() {

    let table = document.getElementById("grid");

    for (let i = 1; i <= 10; i++) {
        //reverse the rows to match the numbering convention
        num = 11 - i;
        r = ""
        if (num < 10) {
            r = "0" + num;
        } else {
            r = num.toString();
        }

        let row = document.createElement("div");
        row.id = "row-" + r;

        table.appendChild(row);
        let row_x = document.getElementById("row-" + r);

        for (let j = 1; j <= 12; j++) {
            let cell = document.createElement("div");

            c = ""
            if (j < 10) {
                c = "0" + j;
            } else {
                c = j.toString();
            }
            
            cell.id = "cell-" + r + "-" + c;

            row_x.appendChild(cell);
        }
    }

    console.log('grid loaded');

    let tbl = document.getElementById("buffer-grid");

    for (let i = 1; i <= 4; i++) {
        
        let buf_row = document.createElement("div");
        buf_row.id = "buffer-grid-row-" + i;

        tbl.appendChild(buf_row);
        let row_y = document.getElementById("buffer-grid-row-" + i);

        for (let j = 1; j <= 24; j++) {
            let buf_cell = document.createElement("div");
            buf_cell.id = "buffer-grid-cell-" + i + "-" + j;

            row_y.appendChild(buf_cell);
        }
    }

    console.log('buffer grid loaded');

    //fetch manifest data from python backend
    fetch("/main-manifest-loaded")
        .then(response => response.json())
        .then(data => {
            console.log(data);
            manifest_list = data
            for (const element of manifest_list) {
                //console.log(element.coordinate)
                id = "cell-" + element.coordinate[0] + "-" + element.coordinate[1]
                //console.log(id);
                document.getElementById(id).innerHTML = element.name;
            }
        })
        .catch(err => { console.log(err); })
}
