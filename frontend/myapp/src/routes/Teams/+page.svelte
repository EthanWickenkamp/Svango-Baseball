<script lang="ts">
  export let data;
  let teams = data.teams;
  let freeAgents = data.freeAgents; 
  let draggedPlayer = null;

  // Extract free agents (players with team: null)
  teams.forEach(team => {
    freeAgents.push(...team.players.filter(player => player.team === null));
    team.players = team.players.filter(player => player.team !== null);
  });

  // Function to handle drag start
  function handleDragStart(event, player) {
    draggedPlayer = player;
    event.dataTransfer.setData("text/plain", JSON.stringify(player));
  }

  // Function to handle drop
  async function handleDrop(event, teamId) {
    event.preventDefault();
    if (!draggedPlayer) return;

    const playerId = draggedPlayer.id; // Store player ID before resetting draggedPlayer

    // Optimistic UI Update (update frontend immediately)
    teams.forEach(team => {
        team.players = team.players.filter(p => p.id !== playerId);
    });

    if (teamId === null) {
        freeAgents = [...freeAgents, draggedPlayer];
    } else {
        let team = teams.find(t => t.id == teamId);
        if (team) {
            team.players = [...team.players, draggedPlayer];
        }
    }

    draggedPlayer.team = teamId;
    draggedPlayer = null;

    // Backend Update
    try {
        const res = await fetch(`/api/players/${playerId}/`, {
            method: "PATCH",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ team: teamId })
        });

        if (!res.ok) {
            console.error("Failed to update player team in backend");
        }

        // 🔥 Re-fetch teams from the backend to ensure UI is accurate
        await refreshTeams();

    } catch (error) {
        console.error("Error updating player:", error);
    }
}

async function refreshTeams() {
    try {
        // Fetch teams (only returns players assigned to a team)
        const teamRes = await fetch('/api/teams/');
        if (!teamRes.ok) throw new Error('Failed to fetch teams');
        const fetchedTeams = await teamRes.json();

        // Fetch free agents separately (players with no team)
        const freeAgentRes = await fetch('/api/players/?team=null');
        let extractedFreeAgents = [];
        if (freeAgentRes.ok) {
            extractedFreeAgents = await freeAgentRes.json();
        }

        teams = fetchedTeams;  // Update teams list
        freeAgents = extractedFreeAgents;  // Update free agents list
    } catch (error) {
        console.error("Error refreshing teams:", error);
    }
}



  function allowDrop(event) {
    event.preventDefault();
  }
</script>

<h1>Team Management</h1>

<div class="team-container">
  {#each teams as team}
    <div 
      class="team"
      on:dragover={allowDrop} 
      on:drop={(e) => handleDrop(e, team.id)}
      role="region"
      aria-label="Drop area"
    >
      <h2>{team.name}</h2>
      <ul>
        {#each team.players as player (player.id)}
          <li 
            draggable="true" 
            on:dragstart={(e) => handleDragStart(e, player)}
          >
            {player.name}
          </li>
        {/each}
      </ul>
    </div>
  {/each}
</div>

<!-- Free Agents -->
<div 
  class="free-agents"
  on:dragover={allowDrop} 
  on:drop={(e) => handleDrop(e, null)}
  role="region"
  aria-label="Drop area"
>
  <h2>Free Agents</h2>
  <ul>
    {#each freeAgents as player (player.id)}
      <li 
        draggable="true" 
        on:dragstart={(e) => handleDragStart(e, player)}
      >
        {player.name}
      </li>
    {/each}
  </ul>
</div>

<style>
  .team-container {
    display: flex;
    gap: 20px;
  }
  .team, .free-agents {
    border: 2px solid #333;
    padding: 10px;
    min-width: 200px;
    background: #f4f4f4;
  }
  ul {
    list-style: none;
    padding-left: 0;
  }
  li {
    margin: 5px 0;
    padding: 5px;
    background: lightgray;
    cursor: grab;
  }
</style>
