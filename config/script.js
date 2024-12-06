// Show welcome message on button click
document.getElementById('welcomeButton').addEventListener('click', function() {
    var message = document.getElementById('welcomeMessage');
    message.style.display = 'block';  // Show the welcome message
});

// Display team details dynamically
function viewTeamDetails(teamId) {
    alert("Details of " + teamId + " will be available soon!");
}

// Dynamic Match List
const matches = [
    { match: "Team 1 vs Team 2", date: "2024-04-01", time: "7:30 PM" },
    { match: "Team 3 vs Team 4", date: "2024-04-02", time: "7:30 PM" },
    // Add more matches as needed
];

const matchList = document.getElementById("match-list");

matches.forEach(match => {
    const li = document.createElement("li");
    li.textContent = `${match.match} - ${match.date} at ${match.time}`;
    matchList.appendChild(li);
});

// Ticket Booking Modal
function openModal() {
    document.getElementById('ticketModal').style.display = 'block';
}

function closeModal() {
    document.getElementById('ticketModal').style.display = 'none';
}

// Booking Tickets (for demo purpose)
document.getElementById('ticket-form').addEventListener('submit', function(event) {
    event.preventDefault();
    const team = document.getElementById('team').value;
    const quantity = document.getElementById('quantity').value;
    alert(`Tickets for ${team} have been booked! Quantity: ${quantity}`);
    closeModal();  // Close modal after booking
});
