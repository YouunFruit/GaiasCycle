document.addEventListener("DOMContentLoaded", async () => {
    const tableBody = document.querySelector("tbody");

    try {
        const response = await fetch("http://localhost:8000/api/tower");
        if (!response.ok) throw new Error("Failed to fetch towers.");

        const towers = await response.json();
        tableBody.innerHTML = towers
            .map(tower => `
                <tr>
                    <td>${tower.id}</td>
                    <td>${tower.farm_id}</td>
                    <td>${tower.slot_amount}</td>
                    <td>${tower.slot_amount}</td>
                    <td>
                        <button class="btn btn-sm btn-primary" onclick="editTower(${tower.id})">Edit</button>
                        <button class="btn btn-sm btn-danger" onclick="deleteTower(${tower.id})">Delete</button>
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
