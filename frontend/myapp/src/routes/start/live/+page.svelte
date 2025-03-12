<script lang="ts">
    export let data: { game: any };
  </script>
  
  <h1>Live Game Information</h1>
  
  {#if data.game}
    <p><strong>Game ID:</strong> {data.game.id}</p>
    <p><strong>Home Team:</strong> {data.game.home_team}</p>
    <p><strong>Away Team:</strong> {data.game.away_team}</p>
    <h2>Selected Players</h2>
    <ul>
      {#each data.game.selected_players as player}
        <li>{player.name} ({player.position})</li>
      {/each}
    </ul>
  {:else}
    <p>Loading game information...</p>
  {/if}
  