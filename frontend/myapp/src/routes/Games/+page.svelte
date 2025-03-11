<script lang="ts">
    import { goto } from '$app/navigation'; // Import navigation function
    export let data;
    let gamesByDay = data.gamesByDay;
  
    function viewGame(gameId) {
      goto(`/games/${gameId}/`); // Navigate dynamically
    }
  </script>
  
  <h1>Game Results by Day</h1>
  
  {#each Object.entries(gamesByDay) as [gameDate, games]}
    <div class="game-day">
      <h2>{new Date(gameDate).toLocaleDateString()}</h2>
      <ul>
        {#each games as game}
          <li>
            <!-- Left-Aligned Button -->
            <button class="view-game-btn" on:click={() => viewGame(game.id)}>
              View Game
            </button>
  
            <!-- Team Names and Scores -->
            <span class="team-name">{game.home_team.name}</span>
            <span class="{game.home_team_score > game.away_team_score ? 'winner-score' : 'loser-score'}">
              {game.home_team_score}
            </span>
            -
            <span class="{game.away_team_score > game.home_team_score ? 'winner-score' : 'loser-score'}">
              {game.away_team_score}
            </span>
            <span class="team-name">{game.away_team.name}</span>
          </li>
        {/each}
      </ul>
    </div>
  {/each}
  
  <style>
    /* Button Styling */
    .view-game-btn {
      background-color: #0077cc;
      color: white;
      border: none;
      padding: 5px 10px;
      cursor: pointer;
      font-size: 1em;
      border-radius: 5px;
      margin-right: 10px; /* Ensures left justification */
    }
  
    .view-game-btn:hover {
      background-color: #005fa3;
    }
  
    /* List Styling */
    li {
      display: flex;
      align-items: center;
      justify-content: flex-start; /* Align content left */
      gap: 15px;
      font-size: 1.2em;
      padding: 10px 0;
    }
  
    /* Other Styles (Team Names, Scores) */
    .team-name {
      font-size: 1.3em;
      font-weight: bold;
      color: #222;
      margin: 0 10px;
    }
  
    .winner-score {
      color: #0077cc;
      font-weight: bold;
      font-size: 1.5em;
    }
  
    .loser-score {
      color: #555;
      font-weight: normal;
      font-size: 1.2em;
    }
  </style>
  