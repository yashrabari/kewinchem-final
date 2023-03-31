module.exports={
   apps:
      [{
        name: "Kewin Chem",
        script: "manage.py",
        args: ["runserver", "0.0.0.0:8080"],
        exec_mode: "cluster",
        instances: "max",
        wait_ready: true,
        autorestart: false,
        max_restarts: 5,
        interpreter : "python3"
      }]
}

