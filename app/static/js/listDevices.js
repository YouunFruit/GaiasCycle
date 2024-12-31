document.addEventListener("DOMContentLoaded", async () => {
    const tableBody = document.querySelector("tbody");

    try {
        const response = await fetch("http://localhost:8000/api/device");
        if (!response.ok) throw new Error("Failed to fetch devices.");

        const devices = await response.json();
        tableBody.innerHTML = devices
            .map(device => `
                <tr>
                    <th onclick="sortTable(0)">${device.id}</th>
                    <th onclick="sortTable(1)">${device.farm_id}</th>
                    <th onclick="sortTable(2)">${device.tower_id}</th>
                    <th onclick="sortTable(3)">${device.slot_id}</th>
                    <th onclick="sortTable(4)">${device.status}</th>
                    <th onclick="sortTable(5)">${device.value}</th>
                    <th onclick="sortTable(6)">${device.unit}</th>
                    <th onclick="sortTable(7)">${device.installation_date}</th>
                    <td>
                        <button class="btn btn-sm btn-primary" onclick="editTower(${device.id})">Edit</button>
                        <button class="btn btn-sm btn-danger" onclick="deleteTower(${device.id})">Delete</button>
                    </td>
                </tr>
            `).join('');
    } catch (error) {
        console.error("Error loading farms:", error);
    }
});

async function deleteTower(farmId) {
    if (!confirm("Are you sure you want to delete this farm?")) return;

    try {
        const response = await fetch(`/api/farms/${farmId}`, { method: "DELETE" });
        if (!response.ok) throw new Error("Failed to delete farm.");
        alert("Farm deleted successfully.");
        location.reload();
    } catch (error) {
        console.error("Error deleting farm:", error);
    }
}
