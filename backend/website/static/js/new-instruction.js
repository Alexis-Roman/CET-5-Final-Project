// document.getElementById('addInstructionButton').addEventListener('click', function() {
//     // Select the HTML container
//     var instruction = document.getElementById('instruction');

//     // Create a copy of the container
//     var containerClone = instruction.cloneNode(true);

//     // Append the container copy to the body (you can append it to another element if needed)
//     parentInstruction.appendChild(containerClone);
// });


var instructionCount = 1;

  document.getElementById('addInstructionButton').addEventListener('click', function() {
    // Increment the count
    instructionCount++;

    // Create a new instruction div
    var newInstructionDiv = document.createElement('div');
    newInstructionDiv.className = 'row';
    newInstructionDiv.id = 'instruction' + instructionCount;
    newInstructionDiv.name = 'instruction' + instructionCount;

    // Add content to the new instruction div
    newInstructionDiv.innerHTML = `
    <div class="container px-3 py-2 post-instruction-title rounded-top text-white" style="background-color: #F06205; height: 70px;">
            <div class="row align-items-center">
                <!-- INSTRUCTION -->
                <div class="col-11 post-instruction">
                    <div class="form-floating">
                        <textarea class="form-control" placeholder="Add instruction here" id="floatingTextarea" style="background-color: #F06205; border: 0px"></textarea>
                        <label for="floatingTextarea">Instruction*</label>
                    </div>
                </div>
                <div class="col-1 d-flex justify-content-center">
                    <div class="btn text-white" onclick="removeInstruction('instruction${instructionCount}')" style="font-size: 30px;">
                        &times;
                    </div>
                </div>
            </div>
        </div>
        <div class="container py-4" style="background-color: white;">
            <!-- IMG -->
            <div class="row">
                <div class="container d-flex justify-content-center my-5" style="background-color: rgb(223, 223, 223);">
                    <div>
                        <form id="imageForm" class="my-5 d-flex-row justify-content-center">
                            <input type="file" id="image_input" accept="image/*"/>
                            <div id="image_display" style="height: 450px; background-position: center; background-size: cover;">
                            </div>
                        </form>
                        <script src="{{ url_for('static', filename='js/image-display.js')}}"></script>
                    </div>
                </div>
            </div>

            <!-- IMG DESCRIPTION -->
            <div class="row pt-2 px-4">
                <div class="form-floating">
                    <textarea class="form-control px-4" placeholder="Leave a comment here" id="floatingTextarea2" style="height: 100px"></textarea>
                    <label class="ms-4" for="floatingTextarea2">Add description here...</label>
                </div>
            </div>
            
        </div>
        <hr>  
    
    `;

    // Append the new instruction div to the parent
    document.getElementById('parentInstruction').appendChild(newInstructionDiv);
  });

  function removeInstruction(instructionId) {
    var instructionDiv = document.getElementById(instructionId);
    instructionDiv.parentNode.removeChild(instructionDiv);
  }