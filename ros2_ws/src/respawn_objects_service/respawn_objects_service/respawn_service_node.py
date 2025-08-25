import rclpy
from rclpy.node import Node
from std_srvs.srv import Trigger
import random

from multiverse_client_py import MultiverseClient, MultiverseMetaData

class RespawnObjectsService(Node):
    def __init__(self):
        super().__init__('respawn_objects_service')

        # Create ROS 2 service
        self.srv = self.create_service(Trigger, 'respawn_objects', self.respawn_callback)

        # Create Multiverse client
        self.client = MultiverseClient(
            host="tcp://127.0.0.1",  # adjust if your Multiverse server is elsewhere
            port="7000",
            multiverse_meta_data=MultiverseMetaData()
        )
        self.get_logger().info('Respawn Objects Service Ready!')

    def respawn_callback(self, request, response):
        # Random positions for cups and balls
        cups = [{'x': random.uniform(1.5, 2.5), 'y': random.uniform(-1, 1)} for _ in range(2)]
        balls = [{'x': random.uniform(1.5, 2.5), 'y': random.uniform(-1, 1)} for _ in range(5)]

        # Send positions to Multiverse
        for i, cup in enumerate(cups):
            self.client.set_object_pose(f"free_cup{i}", pos=[cup['x'], cup['y'], 0.5])
        for i, ball in enumerate(balls):
            self.client.set_object_pose(f"sync_ball{i}", pos=[ball['x'], ball['y'], 0.8 + 0.01*i])

        response.success = True
        response.message = "Objects respawned via Multiverse!"
        self.get_logger().info(response.message)
        return response

def main(args=None):
    rclpy.init(args=args)
    node = RespawnObjectsService()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
