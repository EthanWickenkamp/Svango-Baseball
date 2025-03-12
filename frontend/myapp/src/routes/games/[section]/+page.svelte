<script lang="ts">
  export let data;
  let game = data.game;
  let gameStats = data.game.gamestats;

  if (!gameStats) {
    console.error("GameStats is missing from API response");
  }

  // Get the highest inning number from gameStats (default to 9)
  let maxInning = Math.max(9, ...gameStats.flatMap(stat => stat.atbats.map(atBat => atBat.inning)));

  // Generate inning numbers dynamically (always at least 9 innings)
  let innings = Array.from({ length: maxInning }, (_, i) => i + 1);

  // Collect full player rosters
  let homePlayers = game.home_team.players || [];
  let awayPlayers = game.away_team.players || [];

  // Organize at-bats by inning
  let atBatsByInning = {};

  gameStats.forEach(stat => {
    stat.atbats.forEach(atBat => {
      if (!atBatsByInning[atBat.inning]) {
        atBatsByInning[atBat.inning] = { home: {}, away: {} };
      }

      let teamType = stat.team === game.home_team.name ? "home" : "away";
      
      if (!atBatsByInning[atBat.inning][teamType][stat.player.name]) {
        atBatsByInning[atBat.inning][teamType][stat.player.name] = [];
      }

      atBatsByInning[atBat.inning][teamType][stat.player.name].push(atBat.outcome.replace("_", " "));
    });
  });

</script>

<h1>{game.home_team.name} vs {game.away_team.name} on {new Date(game.game_date).toLocaleDateString()}</h1>

<!-- Home Team At-Bats -->
<h2>{game.home_team.name} <span class="game-score">{game.home_team_score}</span></h2>
<table>
  <thead>
    <tr>
      <th>Player</th>
      {#each innings as inning}
        <th>Inning {inning}</th>
      {/each}
    </tr>
  </thead>
  <tbody>
    {#each homePlayers as player}
      <tr>
        <td>{player.name}</td>
        {#each innings as inning}
          <td>
            {#if atBatsByInning[inning]?.home[player.name]}
              {#each atBatsByInning[inning].home[player.name] as result}
                {result}<br />
              {/each}
            {/if}
          </td>
        {/each}
      </tr>
    {/each}
  </tbody>
</table>

<!-- Away Team At-Bats -->
<h2>{game.away_team.name} <span class="game-score">{game.away_team_score}</span></h2>
<table>
  <thead>
    <tr>
      <th>Player</th>
      {#each innings as inning}
        <th>Inning {inning}</th>
      {/each}
    </tr>
  </thead>
  <tbody>
    {#each awayPlayers as player}
      <tr>
        <td>{player.name}</td>
        {#each innings as inning}
          <td>
            {#if atBatsByInning[inning]?.away[player.name]}
              {#each atBatsByInning[inning].away[player.name] as result}
                {result}<br />
              {/each}
            {/if}
          </td>
        {/each}
      </tr>
    {/each}
  </tbody>
</table>

<button on:click={() => history.back()}>Back</button>

<style>
  h1, h2 {
    color: #000000;
  }

  .game-score {
    font-weight: bold;
    font-size: 1.5em;
    color: #756f94;
    margin: 0 10px;
  }

  table {
    width: 100%;
    border-collapse: collapse;
    margin-top: 20px;
  }

  th, td {
    border: 1px solid #ccc;
    padding: 10px;
    text-align: center;
  }

  th {
    background-color: #f4f4f4;
    font-weight: bold;
  }

  button {
    background-color: #469717;
    color: white;
    border: none;
    padding: 10px 15px;
    cursor: pointer;
    font-size: 1em;
    border-radius: 5px;
    margin-top: 20px;
  }

  button:hover {
    background-color: #469717;
  }
</style>
