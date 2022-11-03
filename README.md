## Instructions

1. Get Anaconda3.

1. Open anaconda Bash, or if you want to use cmd, you'll need to add PATH to env

2. ```bash
   conda create -n steam python=3.8 # steam is just the name of env
   ```

4. Activate environment.

5. ```bash
   conda activate steam
   ```

4. Install latest package.

5. ```bash
   pip install -r requirements.txt
   ```

6. Installed new packages? **Don't forget to export the new requirements!**

7. ```bash
   pip list --format=freeze > requirements.txt
   ```

8. Push your change. **Always pull latest changes before you push!**

9. **If you are downloading data into repo, don’t forget to specify the download path in the `.gitignore` !!!**

## Install Pyspark

1. Make sure your local env is consistent with requirement.txt, if not, install it.
2. Install Java8, make sure PATH is correctly set.
3. Test it with pyspark_test.ipynb
4. **Jupyter Notebook is for test only! Remember to create single .py file for the entire process.**
5. Good reference if you have any question: https://sparkbyexamples.com/pyspark-tutorial/

## Important dates

1. `2018/07/01` Data leak for Steam players count, based on achievements. 

   [Link]: https://arstechnica.com/gaming/2018/07/steam-data-leak-reveals-precise-player-count-for-thousands-of-game

2. `2018/04/11` Valve has made changes to their Steam Web API, removing owned games from user’s information, unless they actively opt-in, which **influences SteamSpy's accuracy!**

   [Link]: https://galyonk.in/whats-going-on-with-steam-spy-deed5d699233

3. 

   

