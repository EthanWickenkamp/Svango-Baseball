<script lang="ts">
    import { goto } from '$app/navigation';
  
    export let data: { 
      teams: { 
        id: number; 
        name: string; 
        players: { id: number; name: string; slug: string; team: number }[] 
      }[] 
    };
  
    let teams = data.teams;
    let homeTeamId: number | null = null;
    let awayTeamId: number | null = null;
    let homeRoster = [];
    let awayRoster = [];
    let selectedPlayers: number[] = [];
    let message = "";
    let loading = false;
  
    function onHomeTeamChange(event: Event) {
      homeTeamId = Number((event.target as HTMLSelectElement).value);
      const team = teams.find(t => t.id === homeTeamId);
      homeRoster = team ? team.players : [];
    }
  
    function onAwayTeamChange(event: Event) {
      awayTeamId = Number((event.target as HTMLSelectElement).value);
      const team = teams.find(t => t.id === awayTeamId);
      awayRoster = team ? team.players : [];
    }
  
    function togglePlayerSelection(playerId: number, event: Event) {
      if ((event.target as HTMLInputElement).checked) {
        selectedPlayers.push(playerId);
      } else {
        selectedPlayers = selectedPlayers.filter(id => id !== playerId);
      }
    }
  
    async function startGame() {
      if (!homeTeamId || !awayTeamId || selectedPlayers.length === 0) {
        message = "Please select both teams and at least one player.";
        return;
      }
      if (homeTeamId === awayTeamId) {
        message = "Home and Away teams must be different.";
        return;
      }
      loading = true;
      message = "";
  
        //trying to get this view to work
      try {
        const response = await fetch("/api/games/start/", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            home_team_id: homeTeamId,
            away_team_id: awayTeamId,
            players: selectedPlayers
          })
        });
  
        const data = await response.json();
        if (response.ok) {
          goto(`/start/${data.game_id}`);
        } else {
          message = data.error || "Error starting game.";
        }
      } catch (error) {
        console.error("Error:", error);
        message = "Failed to connect to the server.";
      } finally {
        loading = false;
      }
    }
  </script>
  
  <h1>Start a New Game</h1>
  
  <p>{message}</p>
  
  <div>
    <label>
      Home Team:
      <select on:change={onHomeTeamChange}>
        <option value="">Select a team</option>
        {#each teams as team}
          <option value={team.id} disabled={team.id === awayTeamId}>{team.name}</option>
        {/each}
      </select>
    </label>
  </div>
  
  <div>
    <label>
      Away Team:
      <select on:change={onAwayTeamChange}>
        <option value="">Select a team</option>
        {#each teams as team}
          <option value={team.id} disabled={team.id === homeTeamId}>{team.name}</option>
        {/each}
      </select>
    </label>
  </div>
  
  {#if homeRoster.length > 0}
    <h2>Home Team Roster</h2>
    {#each homeRoster as player}
      <label>
        <input type="checkbox" on:change={(e) => togglePlayerSelection(player.id, e)} />
        {player.name}
      </label>
    {/each}
  {/if}
  
  {#if awayRoster.length > 0}
    <h2>Away Team Roster</h2>
    {#each awayRoster as player}
      <label>
        <input type="checkbox" on:change={(e) => togglePlayerSelection(player.id, e)} />
        {player.name}
      </label>
    {/each}
  {/if}
  
  <button on:click={startGame} disabled={loading}>
    {loading ? "Starting..." : "Start Game"}
  </button>
  