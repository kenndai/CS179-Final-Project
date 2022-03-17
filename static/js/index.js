
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

    //struct to make sure manifest only loads once
    function gotManifest() {
        gotManifest.state = false;
        gotManifest.count = 0;
    }
    
    var manifest_state = new gotManifest();

    //loads the manifest into the grid boxes when continue button pressed from prior page
    if (!manifest_state.state) {
        manifest_state.state = true;
        manifest_state.count = manifest_state.count + 1;
        console.log("manifest is loaded this many times", manifest_state.count)
        //fetch manifest data from python backend
        fetch("/main-manifest-loaded")
            .then(response => response.json())
            .then(data => {
                //console.log(data);
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

    //balance function called when balance button pressed
    var balance_button = document.getElementById("balance-button");
    var time_arr = []
    balance_button.onclick = function() {
        //fetch steps data from python backend
        fetch("/main", {
            method: "POST",
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify("balance pressed"),
            })
            .then(response => response.json())
            .then(data => {
                console.log(data);

                let total_time = 0;

                //fill move info table html with steps
                //print(f'Move {step["name"]} at {step["orig"]} to {step["new"]} Minutes: {step["minutes"]}')
                let move_table = document.getElementById("move-info-box");

                console.log(data.length)
                for (let i = 1; i < data.length; i++) {
                    //for each step "(step 1:2) Move "
                    let step = document.createElement("div");
                    step.id = "step-" + i;
                    num = data.length-1
                    step.innerHTML = "(Step " + i + ":" + num + ") Move [" + data[i]["orig"][0] + ", " + data[i]["orig"][1] + "] to " + "[" + data[i]["new"][0] + ", " + data[i]["new"][1] + "]"

                    //add total time and record each curr time into global list for later reference
                    time_arr.push(data[i]["minutes"])
                    total_time += parseInt(data[i]["minutes"])

                    move_table.appendChild(step);            
                }

                //assign total est. time
                document.getElementById("total-time").innerHTML = "Total Est. Time: " + total_time + "minutes"

                //assign curr est. time
                if (data.length > 1) {
                    document.getElementById("curr-time").innerHTML = "Est. Time: " + time_arr[0] + "minutes"
                } else {
                    document.getElementById("curr-time").innerHTML = "Est. Time: 0"
                }

            })
            .catch(err => { console.log(err); })
    }

    //modal pop up
    var load_button = document.getElementById("Load-button");
    var container_name_modal = document.getElementById("container-name-modal");
    var num_containers_modal = document.getElementById("num-containers-modal")
    var close = document.getElementsByClassName("delete")[0];
    var num_containers_modal_submit_btn = document.getElementsByClassName("num-containers-modal-submit")[0];
    var container_name_modal_submit_btn = document.getElementsByClassName("container-name-modal-submit")[0];
    var container_count = 0;
    var container_data_arr = []

    // When the user clicks on the button, open the modal
    load_button.onclick = function() {
        num_containers_modal = "block";
    }

    // When the user clicks on submit, record data and open name_modal
    num_containers_modal_submit_btn.onclick = function() {
        container_count = num_containers_modal.value;
        console.log("number of containers", container_count);
        if (container_count != 0) {
            container_name_modal.style.display = "block"; //displays the modal
        }
    }

    // When the user clicks on submit, record data and open name_modal
    container_name_modal_submit_btn.onclick = function() {
        container_data_arr.push(container_name_modal.value);
        if (container_count > 0) {
            container_name_modal.style.display = "block";
            container_count--;
        }
    }
}
