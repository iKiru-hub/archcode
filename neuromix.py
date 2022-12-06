


""" brain.py """

utils = {'generate_substrate': 0,
         'activation_function': 0}

substrate = {'init': 0,
             'step': 0,
             'update': 0,
             'check_dna': 0,
             'initialize': 0,
             'collect_input': 0,
             'add_loss': 0,
             'get_loss': 0,
             'get_output': 0,
             'get_trainable_params': 0,
             'get_trainable_names': 0,
             'get_nb_trainable': 0,
             'is_trainable': 0,
             'get_nb_output': 0,
             'get_substrate_name': 0,
             'get_dna': 0,
             'update_dna': 0,
             'is_initialize': 0,
             'reset': 0}

substrateStructure = {'init': 0,
                      'step': 0,
                      'update': 0,
                      'collect_input': 0,
                      'check_dna': 0,
                      'build_structure': 0,
                      'get_output': 0,
                      'get_activity': 0,
                      'get_trainable_params': 0,
                      'get_trainable_names': 0,
                      'is_trainable': 0,
                      'get_nb_trainable': 0,
                      'get_nb_output': 0,
                      'get_connections': 0,
                      'get_nb_inout': 0,
                      'set_livestream': 0,
                      'add_grapher': 0,
                      'show_graph': 0,
                      'get_grapher': 0,
                      'reset': 0}

protein = {'init': [['Protein', 'check_dna']],
           'step': 0,
           'update': 0,
           'add_loss': 0,
           'check_dna': 0,
           'get_trainable_params': 0,
           'initialize': [['Protein', 'update_dna']],
           'collect_input': 0,
           'get_trainable_params': 0,
           'update_dna': 0,
           'reset': 0}


cell = {'init': [['Cell', 'check_dna'],
                 ['SubstrateStructure', 'build_structure']],
        'check_dna': 0,
        'step': [['Protein', 'get_output'],
                 ['Protein', 'collect_input'],
                 ['Protein', 'step'],
                 ['Protein', 'get_output']],
        'update': [['Protein', 'add_loss'],
                   ['Protein', 'get_loss'],
                   ['Protein', 'update']],
        'build_structure': [['Utils', 'generate_substrate'],
                            ['Protein', 'initialize'],
                            ['Protein', 'get_nb_trainable'],
                            ['Protein', 'get_trainable_names']],
        'get_output': 0,
        'get_activity': 0,
        'get_trainable_params': [['Protein', 'get_trainable_params']],
        'get_trainable_names': 0,
        'is_trainable': 0,
        'get_nb_trainable': 0,
        'get_nb_output': 0,
        'get_connections': 0,
        'get_nb_inout': 0,
        'set_livestream': [['Grapher', 'initialize']],
        'show_graph': [['Grapher', 'draw_graph']],
        'get_grapher': 0,
        'reset': 0
        }


cellPlasticity = {'init': [['Cell', 'check_dna'],
                           ['SubstrateStructure', 'build_structure']],
                  'check_dna': 0,
                  'step': [['Protein', 'get_output'],
                           ['Protein', 'collect_input'],
                           ['Protein', 'step'],
                           ['Protein', 'get_output']],
                  'update': [['Protein', 'add_loss'],
                             ['Protein', 'get_loss'],
                             ['Protein', 'update'],
                             ['Cell', 'collect_internals']],
                  'build_structure': [['Utils', 'generate_substrate'],
                                      ['Protein', 'initialize'],
                                      ['Protein', 'get_nb_trainable'],
                                      ['Protein', 'get_trainable_names']],
                  'collect_internals': 0,
                  'get_output': 0,
                  'get_activity': 0,
                  'get_trainable_params': [['Protein', 'get_trainable_params']],
                  'get_trainable_names': 0,
                  'is_trainable': 0,
                  'get_nb_trainable': 0,
                  'get_nb_output': 0,
                  'get_connections': 0,
                  'get_nb_inout': 0,
                  'set_livestream': [['Grapher', 'initialize']], 
                  'show_graph': [['Grapher', 'draw_graph']],
                  'get_grapher': 0,
                  'reset': 0
                  }


""" Protein instances """

proteinExp = {'init': [['Utils', 'activation_function']],
              'step': 0,
              'update': 0,
              'add_loss': 0,
              'check_dna': 0,
              'get_trainable_params': 0,
              'initialize': [['ProteinExp', 'update_dna']],
              'update_dna': 0,
              'reset': 0}


proteinBase = {'init': [['Utils', 'activation_function']],
               'step': 0,
               'update': 0,
               'add_loss': 0,
               'get_trainable_params': 0,
               'initialize': [['ProteinBase', 'update_dna']],
               'update_dna': 0}


proteinCond = {'init': [['Utils', 'activation_function']],
               'step': 0,
               'update': 0,
               'add_loss': 0,
               'get_trainable_params': 0,
               'initialize': [['ProteinCond', 'update_dna']],
               'update_dna': 0}



""" sim.py """

testmap = {'init': 0,
           'add_input': 0,
           'add_target': 0,
           'rigenerate_data': [['TestMap', 'add_input'],
                               ['TestMap', 'add_target']],
           'plot_stimuli': [['TestMap', 'plot_raster']],
           'plot_raster': 0,
           'testing': [['AgentEvo', 'collect_input'],
                       ['AgentEvo', 'step'],
                       ['AgentEvo', 'get_output'],
                       ['AgentEvo', 'set_fitness']],
           'is_complete': 0,
           }

gym = {'init': 0,
       'add_substrate': ['Substrate', 'initialize'],
       'simulation': [['Substrate', 'is_trainable'],
                      ['Substrate', 'get_nb_output'],
                      ['Substrate', 'get_nb_output'],
                      ['Substrate', 'collect_input'],
                      ['Substrate', 'step'],
                      ['Substrate', 'get_output'],
                      ['Substrate', 'add_loss'],
                      ['Substrate', 'update'],
                      ['TestMap', 'plot_raster']],
       'long_simulation': [['Substrate', 'is_trainable'],
                           ['Substrate', 'get_nb_output'],
                           ['Substrate', 'get_nb_trainable'],
                           ['Substrate', 'get_trainable_names'],
                           ['TestMap', 'rigenerate_data'],
                           ['']],
       'test_substrate': [],
       'plot_classes_test': [],
       'get_input': [],
       'get_target': []}

agentevo = {'init': 0,
            'step': [],
            'collect_input': [],
            'get_output': [],
            'get_fitness': [],
            'get_substrate': [],
            'get_info': 0,
            'get_name': 0,
            'set_fitness': 0,
            'reset': 0}

dna_generator = {'init': 0,
                 'sample_protein': [],
                 'new_dna': [],
                 'generate': [],
                 'mutate': [],
                 'mutate_protein': [],
                 'cross': [],
                 'get_dna': 0}

simple_evolution = {'init': 0,
                    'evolve': [],
                    'new_generation': [],
                    'fit': [],
                    'shell': [],
                    'record': [],
                    'get_fitted_dna': [],
                    'random_name': [],
                    'inherit_name': [],
                    'show_fittest': []}


""" tools.py """

grapher = {'init': [],
           'initialize': [],
           'live_graph': [],
           'draw_graph': [],
           'build': [],
           'set-pause': []}



########################################################

classes_dict = {'Substrate': substrate,
                'SubstrateStructure': substrateStructure,
                'Protein': protein,
                'Cell': cell,
                'CellPlasticity': cellPlasticity,
                'TestMap': testmap,
                'Gym': gym,
                'AgentEvo': agentevo,
                'SimpleEvolution': simple_evolution,
                'DnaGenerator': dna_generator,
                'Grapher': grapher,
                'Utils': utils}

