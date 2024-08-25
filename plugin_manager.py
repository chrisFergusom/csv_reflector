# plugin_manager.py

import os
import importlib.util

class PluginManager:
    def __init__(self):
        self.plugins = {}

    def load_plugins(self, plugin_dir):
        for filename in os.listdir(plugin_dir):
            if filename.endswith('.py') and filename != '__init__.py':
                plugin_name = os.path.splitext(filename)[0]
                plugin_path = os.path.join(plugin_dir, filename)
                spec = importlib.util.spec_from_file_location(plugin_name, plugin_path)
                module = importlib.util.module_from_spec(spec)
                spec.loader.exec_module(module)
                
                if hasattr(module, 'register_plugin'):
                    plugin_info = module.register_plugin()
                    full_name = plugin_info['name']
                    menu, name = full_name.split(':')
                    if menu not in self.plugins:
                        self.plugins[menu] = {}
                    self.plugins[menu][name] = plugin_info

    def get_plugin(self, menu, name):
        return self.plugins.get(menu, {}).get(name)

    def get_all_plugins(self):
        return self.plugins