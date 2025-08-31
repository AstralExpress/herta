import subprocess

import pluggy
from imperium.pathstrider import PATHSTRIDER_MARKER
from imperium.utils import write_to_env

hookimpl = pluggy.HookimplMarker(PATHSTRIDER_MARKER)


class HertaPathstrider:
    def __init__(self):
        self.logger = None
        self.config = None
        self.base_dir = None

    @hookimpl
    def init_plugin(self, logger, config, base_dir):
        self.logger = logger
        self.config = config
        self.base_dir = base_dir
        self.config.update({"base_dir": self.base_dir})

        write_to_env(env_path=base_dir / ".env", config_dict=self.config)
        self.logger.log(f"Herta initialized.")

    @hookimpl
    def start_plugin(self):
        self.logger.log("Herta starting...")
        compose_file = str(self.base_dir / "docker-compose.yml")
        start_docker_cmd = ["docker", "compose", "-f", compose_file, "up", "-d"]

        try:
            self.logger.log(f"Starting Herta with: {' '.join(start_docker_cmd)}")
            subprocess.run(start_docker_cmd, check=True)
            self.logger.log("Herta started successfully.")

        except subprocess.CalledProcessError as e:
            self.logger.log(f"Error starting Herta: {e}")

    @hookimpl
    def stop_plugin(self):
        compose_file = str(self.base_dir / "docker-compose.yml")
        stop_docker_cmd = ["docker", "compose", "-f", compose_file, "down"]

        try:
            self.logger.log(f"Stopping Herta with: {' '.join(stop_docker_cmd)}")
            subprocess.run(stop_docker_cmd, check=True)

        except subprocess.CalledProcessError as e:
            self.logger.log(f"Error while stopping Herta: {e}")

        self.logger.log("Herta stopped.")
