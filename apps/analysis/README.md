# Analysis

This app houses code for running linear pipelines primarily to analyse data.

A pipeline is made up of a number of `steps`. Each step is a callable class that takes a `StepContext` as input
and returns a `StepContext` as output (see `apps.analysis.core.Step`). Most steps extend the `BaseStep` class which
provides some common functionality.

Each step is initialised with a `PipelineContext` before being executed which provides access to logging, global
configuration and other pipeline state.

Files:

* core.py: contains the core pipeline classes
* steps/*: contains the step implementations
* pipeline.py: contains the hard coded pipelines (in future these should be generated from the web UI)
* log.py: contains a logging utility for collecting logs during the pipeline runs
* serializers.py: contains the serializers outputs from the pipeline
* tasks.py: contains the celery tasks for running the pipelines

## Steps

Steps are the building blocks of pipelines.

Step implementations are located in `apps.analysis.steps` and are named according to their function.


## Django models

* Analysis: Configuration for a pipeline. Selects the `source` and `pipeline` which are both IDs of pipelines.
    the `source` pipeline is the pipeline that generates the data to be analysed. The `pipeline` is the pipeline
    that will be run on the data generated by the `source` pipeline.

* RunGroup: The top level grouping of runs. A run group can contain multiple runs of the same pipeline depending
    on whether the source pipeline splits the data into chunks of the pipeline.
    The RunGroup contains the parameters for the pipeline run.

* AnalysisRun: A single run of a pipeline. In the simplest case there will be one for the `source` pipeline and
    one for the `pipeline`. In the case where the `source` pipeline splits the data into chunks
    there will be multiple `AnalysisRun` objects for the `pipeline`.

TODO:
* allow specifying some params when creating the pipline in the UI and others at runtime
  * probably need separate forms for each
* allow user to stop running pipeline from the UI
* better logs view in the UI (filter by log level?)
* better resource handling - perhaps let steps create resources directly via the pipeline context
* lazy loading of resource from DB?
* pass files to assistants
* capture files generated by assistants
* Add name to AnalysisRun e.g. name of group from split data (see `TimeseriesSplitter`)