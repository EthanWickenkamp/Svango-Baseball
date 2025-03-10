<script>
    import { onMount } from "svelte";
  
    let teams = [];
    let selectedTeam = "";
    let players = [];
    let newPlayerName = "";
  
    // Fetch teams when the component mounts.
    onMount(async () => {
      try {
        const res = await fetch("http://localhost:8000/api/teams/");
        teams = await res.json();
      } catch (error) {
        console.error("Error fetching teams:", error);
      }
    });
  
    // Load the roster for the selected team.
    async function loadTeamRoster(teamId) {
      selectedTeam = teamId;
      try {
        // Assuming you have an endpoint for retrieving players by team
        const res = await fetch(`http://localhost:8000/api/teams/${teamId}/players/`);
        players = await res.json();
      } catch (error) {
        console.error("Error fetching roster:", error);
      }
    }
  
    // Add a new player to the roster.
    async function addPlayer() {
      if (!newPlayerName.trim()) return;
      try {
        const res = await fetch("http://localhost:8000/api/players/", {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ name: newPlayerName, team: selectedTeam }),
        });
        if (res.ok) {
          const addedPlayer = await res.json();
          players = [...players, addedPlayer];
          newPlayerName = "";
        } else {
          console.error("Failed to add player");
        }
      } catch (error) {
        console.error("Error adding player:", error);
      }
    }
  
    // Remove a player from the roster.
    async function removePlayer(playerId) {
      try {
        const res = await fetch(`http://localhost:8000/api/players/${playerId}/`, {
          method: "DELETE",
        });
        if (res.ok) {
          players = players.filter(player => player.id !== playerId);
        } else {
          console.error("Failed to remove player");
        }
      } catch (error) {
        console.error("Error removing player:", error);
      }
    }
  </script>
  
<h1>Welcome to Teams page</h1>
  
  <!-- Dropdown to select a team -->
  <select on:change="{(e) => loadTeamRoster(e.target.value)}">
    <option value="">Select a team</option>
    {#each teams as team}
      <option value="{team.id}">{team.name}</option>
    {/each}
  </select>
  
  {#if selectedTeam}
    <h2>Roster for Team {selectedTeam}</h2>
    <ul>
      {#each players as player (player.id)}
        <li>
          {player.name} 
          <button on:click="{() => removePlayer(player.id)}">Remove</button>
        </li>
      {/each}
    </ul>
  
    <input
      type="text"
      placeholder="New player name"
      bind:value="{newPlayerName}"
    />
    <button on:click="{addPlayer}">Add Player</button>
  {/if}
  
  <style>
    /* Basic styling; adjust as needed */
    h1, h2 {
      font-family: Arial, sans-serif;
    }
    select, input, button {
      margin: 0.5em 0;
    }
    ul {
      list-style: none;
      padding-left: 0;
    }
    li {
      margin: 0.5em 0;
    }
  </style>
  