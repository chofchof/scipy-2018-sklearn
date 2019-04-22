SciPy Tutorial 2: Machine learning with scikit-learn
================================

- [조진환](https://chofchof.github.io/)  [@chofchof](https://github.com/chofchof) - 국가수리과학연구소, 산업수학혁신센터

----

이 리포지토리는 2019년 4월 25일 (PM 13:30~17:30) 산업수학혁신센터에서 열린 2019년 1차 산업수학 모더레이터 역량강화 프로그램 2일차 튜토리얼 자료를 담고 있습니다.

이 자료는 2018년 7월 9-15일 미국 텍사스 오스틴에서 열린 [SciPy 2018](http://scipy2018.scipy.org/) 에서 [Guillaume Lemaitre](https://glemaitre.github.io/) 와 [Andreas Mueller](http://amuller.github.io) 가 진행한 [Scikit-learn 튜토리얼 자료](https://github.com/amueller/scipy-2018-sklearn)를 포크한 후 수정한 것입니다.


패키지 설치
------------------

이 튜토리얼은 Python 3.7 버전을 기반으로 아래와 같은 패키지들을 사용합니다.

- [NumPy](http://www.numpy.org)
- [SciPy](http://www.scipy.org)
- [matplotlib](http://matplotlib.org)
- [pandas](http://pandas.pydata.org)
- [pillow](https://python-pillow.org)
- [scikit-learn](http://scikit-learn.org/stable/)
- [JupyterLab](https://jupyterlab.readthedocs.io)

[Anaconda3](https://www.anaconda.com/distribution/) 또는 [Miniconda3](https://repo.continuum.io/miniconda/)이 미리 설치되어 있는 상태에서

1. `environment.yml` 파일을 [https://raw.githubusercontent.com/dlimpid/nims-moderator-2019-04/master/environment.yml](https://raw.githubusercontent.com/dlimpid/nims-moderator-2019-04/master/environment.yml) 에서 다운로드합니다.
2. 터미널 (윈도의 경우 Anaconda Prompt)을 열고 다음 명령을 실행하면 `moderator-tutorial` 환경이 만들어집니다.

   ```bash
   conda env create -f environment.yml 
   ```

자료 다운로드
------------------

자료를 처음 다운로드하는 경우 아래의 명령을 사용하면 리포지토리를 복사할 수 있습니다.

```bash
git clone https://github.com/chofchof/scipy-2018-sklearn.git
```

이미 자료를 다운로드한 경우 아래의 명령을 사용하면 변경된 내용만 가져올 수 있습니다.

```bash
git pull
```

JupyterLab 실행
------------------

JupyterLab은 다음 명령으로 실행할 수 있습니다.

```bash
conda activate moderator-tutorial
jupyter-lab 
```

먼저 `check_env.ipynb` 파일을 연 후 코드를 실행해 다음 결과가 나오는 지 체크합니다.

```python
Using python in /opt/conda/envs/moderator-tutorial
3.7.3 (default, Mar 27 2019, 16:54:48) 
[Clang 4.0.1 (tags/RELEASE_401/final)]

[ OK ] numpy version 1.16.2
[ OK ] scipy version 1.2.1
[ OK ] matplotlib version 3.0.3
[ OK ] pandas version 0.24.2
[ OK ] sklearn version 0.20.3
[ OK ] PIL version 6.0.0
```

데이터 다운로드
--------------

~~데이터 다운로드는 다음 명령으로 수행할 수 있습니다.~~
```bash
python fetch_data.py
```

목차
=======

- 01 Introduction to machine learning with sample applications, Supervised and Unsupervised learning [[view](notebooks/01.Introduction_to_Machine_Learning.ipynb)]
- 02 Scientific Computing Tools for Python: NumPy, SciPy, and matplotlib [[view](notebooks/02.Scientific_Computing_Tools_in_Python.ipynb)]
- 03 Data formats, preparation, and representation [[view](notebooks/03.Data_Representation_for_Machine_Learning.ipynb)]
- 04 Supervised learning: Training and test data [[view](notebooks/04.Training_and_Testing_Data.ipynb)]
- 05 Supervised learning: Estimators for classification [[view](notebooks/05.Supervised_Learning-Classification.ipynb)]
- 06 Supervised learning: Estimators for regression analysis [[view](notebooks/06.Supervised_Learning-Regression.ipynb)]
- 07 Unsupervised learning: Unsupervised Transformers [[view](notebooks/07.Unsupervised_Learning-Transformations_and_Dimensionality_Reduction.ipynb)]
- 08 Unsupervised learning: Clustering [[view](notebooks/08.Unsupervised_Learning-Clustering.ipynb)]
- 09 The scikit-learn estimator interface [[view](notebooks/09.Review_of_Scikit-learn_API.ipynb)]
- 10 Preparing a real-world dataset (titanic) [[view](notebooks/10.Case_Study-Titanic_Survival.ipynb)]
- 11 Working with text data via the bag-of-words model [[view](notebooks/11.Text_Feature_Extraction.ipynb)]
- 12 Application: IMDb Movie Review Sentiment Analysis [[view](notebooks/12.Case_Study-SMS_Spam_Detection.ipynb)]

- 13 Cross-Validation [[view](notebooks/13.Cross_Validation.ipynb)]
- 14 Model complexity and grid search for adjusting hyperparameters [[view](notebooks/14.Model_Complexity_and_GridSearchCV.ipynb)]
- 15 Scikit-learn Pipelines [[view](notebooks/15.Pipelining_Estimators.ipynb)]
- 16 Supervised learning: Performance metrics for classification [[view](notebooks/16.Performance_metrics_and_Model_Evaluation.ipynb)]
- 17 Supervised learning: Linear Models [[view](notebooks/17.In_Depth-Linear_Models.ipynb)]
- 18 Supervised learning: Decision trees and random forests, and ensemble methods [[view](notebooks/18.In_Depth-Trees_and_Forests.ipynb)]
- 19 Supervised learning: feature selection [[view](notebooks/19.Feature_Selection.ipynb)]
- 20 Unsupervised learning: Hierarchical and density-based clustering algorithms [[view](notebooks/20.Unsupervised_learning-Hierarchical_and_density-based_clustering_algorithms.ipynb)]
- 21 Unsupervised learning: Non-linear dimensionality reduction [[view](notebooks/21.Unsupervised_learning-Non-linear_dimensionality_reduction.ipynb)]
- 22 Unsupervised learning: Anomaly Detection [[view](notebooks/22.Unsupervised_learning-anomaly_detection.ipynb)]
- 23 Supervised learning: Out-of-core learning [[view](notebooks/23.Out-of-core_Learning_Large_Scale_Text_Classification.ipynb)]
