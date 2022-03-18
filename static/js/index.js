
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
            cell.setAttribute("text", "")
            cell.setAttribute("weight", "")
            //cell.className += "cell"

            cell.onclick = function() {
                if (balance_pressed == false) {
                    //highlight the grid cell
                    $(this).toggleClass("highlight-3")

                    //display the grid cell contents on the right side bar
                    let move_table = document.getElementById("moves")
                    move_table.innerHTML = ""

                    if (this.getAttribute("text") != "") {                 
                        let text_div = document.createElement("div");
                        text_div.id = "cell-info"
                        text_div.innerHTML = "<b>Name: </b>" + this.getAttribute("text");
                        move_table.appendChild(text_div);

                        let weight_div = document.createElement("div");
                        weight_div.id = "cell-info"
                        weight_div.innerHTML = "<b>Weight: </b>" + this.getAttribute("weight") + " lbs";
                        move_table.appendChild(weight_div);
                    }
                }
            }

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

            buf_cell.setAttribute("text", "")
            buf_cell.setAttribute("weight", "")
            //buf_cell.className += "cell"

            buf_cell.onclick = function() {
                if (balance_pressed == false) {
                    $(this).toggleClass("highlight-3")

                    //display the grid cell contents on the right side bar
                    if ((this.getAttribute("text") != "") && (balance_pressed == false)) {
                        move_table = document.getElementById("moves")
                        move_table.innerHTML = ""

                        let text_div = document.createElement("div");
                        text_div.id = "cell-info"
                        text_div.innerHTML = "<b>Name: </b>" + this.getAttribute("text");
                        move_table.appendChild(text_div);

                        let weight_div = document.createElement("div");
                        weight_div.id = "cell-info"
                        weight_div.innerHTML = "<b>Weight: </b>" + this.getAttribute("weight") + " lbs";
                        move_table.appendChild(weight_div);
                    }
                }
            }

            row_y.appendChild(buf_cell);
        }
    }

    console.log('buffer grid loaded');


}

//highlights on click
$('div').click(function() {
    $('.cell').toggleClass('highlight-3');
    
});




var load_list = []
var balance_pressed = false

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
                //add 0 to the numbers for consistent formatting
                let id = ""
                if (element.coordinate[0] < 10) {
                    id = "cell-0" + element.coordinate[0]
                } else {
                    id = "cell-" + element.coordinate[0]
                }
                if (element.coordinate[1] < 10) {
                    id += "-0" + element.coordinate[1]
                } else {
                    id += "-" + element.coordinate[1]
                }
                //console.log(id);
                var grid_cell = document.getElementById(id)
                grid_cell.innerHTML = element.name;
                grid_cell.setAttribute("text", element.text)
                grid_cell.setAttribute("weight", element.weight)
            }
        })
        .catch(err => { console.log(err); })
}

//balance function called when balance button pressed
var balance_button = document.getElementById("balance-button");
var time_dict = {}
var previous_line_unhighlighted = ""
var curr_step = 1
var total_time = 0
var steps

balance_button.onclick = function() {
    balance_pressed = true

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
            //console.log(data);

            steps = data
            total_time = 0;
            time_dict = {}
            previous_line_unhighlighted = ""
            curr_step = 1

            //fill move info table html with steps
            //print(f'Move {step["name"]} at {step["orig"]} to {step["new"]} Minutes: {step["minutes"]}')
            let move_table = document.getElementById("moves");
            move_table.innerHTML = ""

            for (let i = 1; i < data.length; i++) {
                //for each step "(step 1:2) Move "
                let step = document.createElement("div");
                step.id = "step-" + i;
                num = data.length-1

                //add 0 to the numbers for consistent formatting
                let row0 = ""
                if (data[i]["orig"][0] < 10) {
                    row0 = "0" + data[i]["orig"][0]
                } else {
                    row0 = data[i]["orig"][0]
                }
                let col0 = ""
                if (data[i]["orig"][0] < 10) {
                    col0 = "0" + data[i]["orig"][1]
                } else {
                    col0 = data[i]["orig"][1]
                }
                let row1 = ""
                if (data[i]["new"][0] < 10) {
                    row1 = "0" + data[i]["new"][0]
                } else {
                    row1 = data[i]["new"][0]
                }
                let col1 = ""
                if (data[i]["new"][0] < 10) {
                    col1 = "0" + data[i]["new"][1]
                } else {
                    col1 = data[i]["new"][1]
                }

                step.innerHTML = "(" + i + " of " + num + ") Move [" + row0 + ", " + col0 + "] to " + "[" + row1 + ", " + col1 + "]"

                //add total time and record each curr time into global list for later reference
                time_dict[""+i] = data[i]["minutes"]
                total_time += parseInt(data[i]["minutes"])

                move_table.appendChild(step);            
            }

            //assign total est. time
            document.getElementById("total-time").innerHTML = "Total Est. Time: " + total_time + " minutes"

            //assign curr est. time
            if (data.length > 1) {
                document.getElementById("curr-time").innerHTML = "Est. Time: " + time_dict["1"] + " minutes"
            } else {
                document.getElementById("curr-time").innerHTML = "Est. Time: 0"
            }

            //highlight step 1
            let first_step = document.getElementById("step-1")
            let innerHTML = first_step.innerHTML;
            previous_line_unhighlighted = first_step.innerHTML;
            innerHTML = innerHTML.substring(0, 14) + "<span class='highlight-1'>" + innerHTML.substring(14, 22) + "</span>"
                + innerHTML.substring(22, 26) + "<span class='highlight-2'>" + innerHTML.substring(26, 34) + "</span>";
            first_step.innerHTML = innerHTML;

            //highlight boxes
            cell_id = getCellID(steps, 1, "orig")
            document.getElementById(cell_id).style.backgroundColor = "#ff00bf"

            cell_id = getCellID(steps, 1, "new")
            document.getElementById(cell_id).style.backgroundColor = "#FFFF00"

        })
        .catch(err => { console.log(err); })
}

//next button pressed
document.getElementById("next-button").onclick = function() {      
    //unhighlight previous line and update total minutes
    if (balance_pressed) {
        if (curr_step <= Object.keys(time_dict).length) {
            let id = "step-" + curr_step
            document.getElementById(id).innerHTML = previous_line_unhighlighted

            //move the box
            orig_cell_id = getCellID(steps, curr_step, "orig")
            new_cell_id = getCellID(steps, curr_step, "new")
            temp_html = document.getElementById(orig_cell_id).innerHTML
            document.getElementById(orig_cell_id).innerHTML = document.getElementById(new_cell_id).innerHTML
            document.getElementById(new_cell_id).innerHTML = temp_html           

            //unhighlight boxes
            document.getElementById(orig_cell_id).style.backgroundColor = "white";
            document.getElementById(new_cell_id).style.backgroundColor = "white";

            //update the total minutes
            total_time -= time_dict[curr_step + ""]
            document.getElementById("total-time").innerHTML = "Total Est. Time: " + total_time + " minutes"

            //send post request to update backend cell shift
        }

        //goto next step
        curr_step++

        //highlight next line and update current minutes
        if (curr_step <= Object.keys(time_dict).length) {
            //highlight next
            let next_id = "step-" + curr_step
            let next_step = document.getElementById(next_id)
            let innerHTML = next_step.innerHTML;
            previous_line_unhighlighted = next_step.innerHTML;
            innerHTML = innerHTML.substring(0, 14) + "<span class='highlight-1'>" + innerHTML.substring(14, 22) + "</span>"
                + innerHTML.substring(22, 26) + "<span class='highlight-2'>" + innerHTML.substring(26, 34) + "</span>";
            next_step.innerHTML = innerHTML;

            //highlight boxes
            cell_id = getCellID(steps, curr_step, "orig")
            document.getElementById(cell_id).style.backgroundColor = "#ff00bf"

            cell_id = getCellID(steps, curr_step, "new")
            document.getElementById(cell_id).style.backgroundColor = "#FFFF00"

            //update curr time
            document.getElementById("curr-time").innerHTML = "Est. Time: " + time_dict[curr_step + ""] + " minutes"

        } else {
            //last step just finished
            document.getElementById("curr-time").innerHTML = "Est. Time: 0"

            //change balance status flag back to false and pop balance msg modal
            balance_pressed = false
            document.getElementById("balanced-modal").style.display = "block";
        }
    }


}

//modal pop up
var load_button = document.getElementById("Load-button");
var num_containers_modal = document.getElementById("num-containers-modal");
var num_containers_modal_submit_btn = document.getElementsByClassName("num-containers-modal-submit")[0];
var container_text = document.getElementById("container-text");

var weight_modal = document.getElementById("weight-entry-modal");
var weight_modal_submit_btn = document.getElementById("weight-modal-submit");
var weight_modal_weight = document.getElementById("weight");
var weight_modal_text = document.getElementById("weight-entry-modal");

// When the user clicks on the button, open the modal
load_button.onclick = function() {
    num_containers_modal = "block";
}

// When the user clicks on submit, record data and open name_modal
num_containers_modal_submit_btn.onclick = function() {
    container_str = container_text.value;
    //parse and update global list variable
    load_list = container_str.split(",").map(function (value) {
        return value.trim();
    });
}

load_button.onclick = function() {
    num_containers_modal = "block";
}

//after weight modal pops up, when submit button pressed
weight_modal_submit_btn.onclick = function() {
    //post request and send into back to python
    var container_dict = {};
    var weight = weight_modal_weight.value
    var name = weight_modal_text.value

    container_dict.push({
        key:   weight,
        value: name
    });

    fetch("/main", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(container_dict),
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);
        //get coordinates and make new container on grid

        //send modal that notifies the operator where to place new container
        document.getElementById("coordinates").innerHTML = "Move Container " + name + " to Coordinates [" + data[0] + ", " + data[1] + "]"
        document.getElementById("coordinate-modal").style.display = "block";
        
        let id = ""
        if (data[0] < 10) {
            id = "cell-0" + data[0]
        } else {
            id = "cell-" + data[0]
        }
        if (data[1] < 10) {
            id += "-0" + data[1]
        } else {
            id += "-" + data[1]
        }
        //console.log(id);
        document.getElementById(id).innerHTML = name;
        document.getElementById(id).style.backgroundColor = "#ff00bf";
        
    })
    .catch(err => { console.log(err); })

}

//balance modal popped up because last step was executed
document.getElementById("balanced-finished").onclick = function() {
    document.getElementById("balanced-modal").style.display = "none";
    document.getElementById("finish-modal").style.display = "block";
}

document.getElementById("finish-modal-got-it").onclick = function() {
    document.getElementById("finish-modal").style.display = "none";
}

document.getElementById("balanced-modal-delete").onclick = function() {
    document.getElementById("balanced-modal").style.display = "none";
}

document.getElementById("finish-modal-delete").onclick = function() {
    document.getElementById("finish-modal").style.display = "none";
}

function getCellID(steps, i, str) {
    cell_id = ""
    if (steps[i][str][0] < 10) {
        cell_id = "cell-0" + steps[i][str][0]
    } else {
        cell_id = "cell-" + steps[i][str][0]
    }
    if (steps[i][str][1] < 10) {
        cell_id += "-0" + steps[i][str][1]
    } else {
        cell_id += "-" + steps[i][str][1]
    }
    return cell_id
}
