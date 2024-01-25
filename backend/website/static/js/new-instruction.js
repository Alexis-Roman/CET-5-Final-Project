document.getElementById('addInstructionButton').addEventListener('click', function() {
    // Select the HTML container
    var instruction = document.getElementById('instruction');

    // Create a copy of the container
    var containerClone = instruction.cloneNode(true);

    // Append the container copy to the body (you can append it to another element if needed)
    parentInstruction.appendChild(containerClone);
});