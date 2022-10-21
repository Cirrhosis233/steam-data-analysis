## Instructions

1. Get Anaconda3.

2. ```bash
   conda create -n steam python=3.8 # steam is just the name of env
   ```

3. Activate environment.

4. Install latest package.

5. ```bash
   pip install -r requirements.txt
   ```

6. Installed new packages? **Don't forget to export the new requirements!**

7. ```bash
   pip list --format=freeze > requirements.txt
   ```

8. Push your change. **Always pull latest changes before you push!**

8. **If you are downloading data into repo, don’t forget to specify the download path in the `.gitignore` !!!**

## Important dates

1. `2018/07/01` Data leak for Steam players count, based on achievements. 

   [Link]: https://arstechnica.com/gaming/2018/07/steam-data-leak-reveals-precise-player-count-for-thousands-of-game

2. `2018/04/11` Valve has made changes to their Steam Web API, removing owned games from user’s information, unless they actively opt-in, which **influences SteamSpy's accuracy!**

   [Link]: https://galyonk.in/whats-going-on-with-steam-spy-deed5d699233

3. 

   

