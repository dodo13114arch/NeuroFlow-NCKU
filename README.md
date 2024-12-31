# NeuroFlow -NCKU

# NeuroFlow
Designer: WeiPing Chang 張偉平 
***

![image_example](/images/NeuroFlow/neuroflow_a.png)

## 研究主題 Research Topic

結合大型語言模型之人流模擬框架應用於建築設計

Application of a Pedestrian Simulation Framework Integrated with Large Language Models in Architecture Design

## 摘要 Abstract

本研究提出NeuroFlow人流行為模擬框架，旨在模擬具有非單一目標與特定行動的人流行為。此類活動通常目的性較弱（如隨意閒逛）、目標較廣泛（如逛街「隨意看看」、參觀美術館「逛完所有展廳」），或具有多目標情境（各目標達成即可，無特定順序）。在這些情境下，行人大多無預設行程順序或路徑規劃，且經常因發現新的興趣點而改變行動。本研究基於Flow人流模擬框架（Izaki et al., 2022），並引入大型語言模型（Large Language Model, LLM），使模擬代理人（Agent）具備即時決策與判斷能力。

本系統旨在提升多功能空間（如大廳、中庭廣場）及空間機能轉換（如舊校舍改建為新博物館等）中的人流模擬準確性。同時，代理人以第一人稱視角結合自然語言回饋空間體驗，有助於分析過去較難量化的指標（如感受、空間氛圍等）。NeuroFlow將整合於建築設計常用的建模平台（如Rhino, Grasshopper），幫助建築設計專業人員在設計初期驗證預期人流，作為優化設計的參考。未來，NeuroFlow可進一步結合建築資訊模型（Building Information Modeling, BIM），以擴充並完善整體模擬框架。

This study introduces the NeuroFlow pedestrian behavior simulation framework, which aims to simulate pedestrian behavior characterized by non-singular objectives and specific actions. Such activities often have weaker intentionality (e.g., casual strolling), broader goals (e.g., window shopping with no specific items in mind, visiting an art museum with the intent to "see all the exhibits"), or multi-goal scenarios (where achieving any goal suffices, with no specific sequence). In these situations, pedestrians usually lack a predefined itinerary or path plan and frequently adjust their actions upon discovering new points of interest.

Building on the Flow pedestrian simulation framework (Izaki et al., 2022), this research incorporates a Large Language Model (LLM) to enable simulation agents to make real-time decisions and judgments. The system aims to enhance the accuracy of pedestrian simulations in multifunctional spaces (e.g., lobbies, atrium plazas) and during spatial function transitions (e.g., repurposing an old school building into a new museum). Additionally, agents provide first-person perspective feedback using natural language, offering insights into previously difficult-to-quantify metrics such as perceived ambiance and spatial atmosphere.

The system is integrated into architectural design modeling platforms commonly used by professionals (e.g., Rhino, Grasshopper), assisting designers in validating expected pedestrian flows during the early design stages to optimize their designs. Looking ahead, this system can be further expanded by integrating with Building Information Modeling (BIM) to enhance and refine the overall simulation framework.

## 研究背景 Research Background

NeuroFlow，受 Schaumann, D.等人 (2016) 提出的Event Modeling Language (EML) 模擬系統及其後續研究、Izaki, Å.等人 (2022) 提出的Flow: Agent Simulation Framework with Spatial Choice for Multilevel Buildings以及其後續研究應用所啟發。並結合Generative Agents: Interactive Simulacra of Human Behavior(Park, J. S., et al., 2023) 中”由大型語言模型 (LLM) 主導生成式代理人的行為，使Agent具備反思、決策能力”的概念。嘗試將人流模擬框架與LLM結合，期望對於使模擬分析本身更接近真實行人的行為，並且將此模擬框架應用於建築設計領域。


<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
  <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
          src="https://www.youtube.com/embed/s-FNhalqGvs" 
          title="YouTube video player" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen>
  </iframe>
</div>
<p style="text-align: center;"><em>EML Demo by Schaumann, D.</em></p>

<div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; max-width: 100%; background: #000;">
  <iframe style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" 
          src="https://www.youtube.com/embed/ZdoU9vI2yCg?si=DwGfysEnp8Vb6xbP" 
          title="YouTube video player" 
          frameborder="0" 
          allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" 
          allowfullscreen>
  </iframe>
</div>
<p style="text-align: center;"><em>Generative Agents: Interactive Simulacra of Human Behavior Demo </em></p>

NeuroFlow, inspired by the Event Modeling Language (EML) simulation system proposed by Schaumann, D., et al. (2016) and its subsequent applications, as well as the Flow: Agent Simulation Framework with Spatial Choice for Multilevel Buildings by Izaki, Å., et al. (2022) and its later developments. It incorporates the concept from *Generative Agents: Interactive Simulacra of Human Behavior* (Park, J. S., et al., 2023), which emphasizes the use of Large Language Models (LLMs) to enable generative agents with reflection and decision-making capabilities.

By integrating LLMs into the pedestrian simulation framework, this research aims to create simulations that more closely mirror the behavior of real pedestrians. Furthermore, it explores the application of this enhanced simulation framework in the field of architectural design.

## 研究方法 Methodology

首先針對現有人流模擬系統蒐集資料 (表.1) ，歸納出目前較多人流模擬系統為專業商用軟體、或基於其他軟體的環境，導致較難於建築設計初期應用。而目前免費提供大眾使用且針對Grasshopper所開發的人流行為模擬外掛 (plugin) 僅有Pedsim、Quelea。其中Pedsim在資料收集此刻已停止開發並下架，而Quelea則是開源 (open source) 軟體，可於Github上獲取其開源程式碼。Quelea本身並非僅針對人流模擬開發，其理論基礎主要基於”代理人基模型”（Agent-Based Modeling, ABM）和群體動力學（Swarm Dynamics），這類模型模擬個體（agent）通過簡單規則（如避障、追隨、對齊）與環境和其他代理交互，進而展現出複雜的集體行為。經過檢視Quelea的開源程式碼，我認為不適合直接修改以重現Flow系統框架。在研究初期，我嘗試在Grasshopper環境中透過內建的python component 進行Flow系統架構的重現。但由於Grasshopper運算的邏輯及其性能限制，即使透過Compas Eve框架將部分程式碼於外部Python環境運算，也因Grasshopper Python語言版本衝突較難重構Flow架構。因此後來轉向在外部純Python環境下重構Flow系統架構，並預期未來待NeuroFlow系統架構成熟將透過Compas框架下RPC (Remote Procedure Call) 的方式讓使用者可直接於Grasshopper環境調用NeuroFlow。

![image_example](/images/NeuroFlow/table_plugin.png)
<p style="text-align: center;"><em>Table.1 現有人流模擬軟體</em></p>

![image_example](/images/NeuroFlow/compas_eve_test.png)
<p style="text-align: center;"><em>Fg.2 左圖：聚積係數可見性分析  中、右圖：Compas Eve 外部運算測試</em></p>


Firstly, data on existing pedestrian simulation systems was collected (Table 1), revealing that most current systems are either professional commercial software or rely on other software environments, making them less applicable during the early stages of architectural design. Among the publicly available and Grasshopper-targeted plugins for pedestrian behavior simulation, only Pedsim and Quelea were identified. At the time of this research, Pedsim had ceased development and was no longer available, while Quelea is an open-source software accessible on GitHub.

Quelea is not specifically designed for pedestrian simulation but is instead grounded in the principles of "Agent-Based Modeling" (ABM) and "Swarm Dynamics." These models simulate the interactions of individual agents with their environment and each other based on simple rules (e.g., obstacle avoidance, following, alignment), resulting in emergent complex collective behavior. After reviewing Quelea's open-source code, it was determined that it was not suitable for directly modifying to replicate the Flow system framework.

During the early stages of this research, an attempt was made to recreate the Flow system architecture within the Grasshopper environment using its built-in Python components. However, due to the computational logic and performance limitations of Grasshopper, even leveraging the Compas Eve framework to offload some computations to an external Python environment proved challenging. Version conflicts with Grasshopper’s Python interpreter further complicated efforts to reconstruct the Flow architecture.

Consequently, the approach shifted to fully rebuilding the Flow system architecture in a standalone Python environment. It is anticipated that once the NeuroFlow system architecture matures, it will integrate with Grasshopper through RPC (Remote Procedure Call) within the Compas framework, allowing users to directly invoke NeuroFlow functionalities in Grasshopper.

## NeuroFlow 模擬框架 Simulation Architecture

### 簡述Flow框架　Overview of the Flow: Agent Simulation Framework

簡述Flow 系統架構，


![image_example](/images/NeuroFlow/flow_step.png)
<p style="text-align: center;"><em>Fg.3 Flow模擬架構流程 (參考 Izaki et al., 2022)</em></p>


### NeuroFlow 框架設計

基於上述架構

![image_example](/images/NeuroFlow/neuroflow_step.png)
<p style="text-align: center;"><em>Fg.4 NeuroFlow模擬架構流程 </em></p>


## Demo

<video controls width=100% preload="metadata">
  <source src="/videos/demo_v1.mp4" type="video/mp4" />
  Your browser does not support the video tag.
</video>

<p style="text-align: center;"><em>NeuroFlow Demo </em></p>

## 研究分析結果 Analysis Result

以下測試目前版本的程式，以奇美博物館的一樓作為測試場景，因效能、時間因素，且對於瀏覽展示品這類行為（Browse）尚未實作，因此著重於博物館大廳的部分，省略處以常設展區（Permanent_Exhibition_Area）表示。特展區的平面配置，假設當下奇美博物館正主辦《從拉斐爾到梵谷：英國國家藝廊珍藏展》，依照其展覽室位置進行設置。並假設館方在此同時，考慮在大廳中央佈置一顆巨大的且會遮蔽視線的聖誕樹。將兩種場景分別進行模擬並比較結果。輸入行程(task)如下：

```json
[
    {"type": "navigate", "description": "導航至 Ticketoffice", "target": "Ticketoffice"},
    {"type": "wander", "description": "閒晃", "duration": 5.0},
    {"type": "navigate", "description": "導航至 GalleryB_Art1", "target": "GalleryB_Art1"},
    {"type": "wander", "description": "閒晃", "duration": 5.0},
    {"type": "navigate", "description": "導航至 GalleryA_Art1", "target": "GalleryA_Art1"},
    {"type": "navigate", "description": "導航至 Cafe", "target": "Cafe"}
]
```

### 人流分析圖 Path Map
<style>
* { box-sizing: border-box; }

.img-comp-container {
  position: relative;
  height: auto; /* 自動調整高度 */
  width: 100%; /* 填滿父容器 */
  aspect-ratio: 1 / 1; /* 維持3:2比例（300px:200px） */
  overflow: hidden;
}


.img-comp-container img {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.img-comp-overlay {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  clip-path: inset(0 50% 0 0); /* 初始裁剪範圍 */
}

.img-comp-slider {
  position: absolute;
  z-index: 10;
  cursor: ew-resize;
  /* 滑桿樣式設定 */
  width: 20px;
  height: 20px;
  background-color: #2196F3;
  opacity: 0.7;
  border-radius: 50%;
  transform: translate(-50%, -50%);
}
</style>

<div class="img-comp-container">
  <img src="/images/NeuroFlow/FPM1.png" alt="Image 1">
  <div class="img-comp-overlay">
    <img src="/images/NeuroFlow/FPM2.png" alt="Image 2">
  </div>
  <div class="img-comp-slider" style="top: 50%; left: 50%;"></div>
</div>

<script>
function initComparisons() {
  var container = document.querySelector(".img-comp-container");
  var overlay = document.querySelector(".img-comp-overlay");
  var slider = document.querySelector(".img-comp-slider");

  var containerWidth = container.offsetWidth;

  // 初始化滑桿拖動行為
  slider.addEventListener("mousedown", startDragging);
  window.addEventListener("mouseup", stopDragging);
  window.addEventListener("mousemove", drag);

  slider.addEventListener("touchstart", startDragging);
  window.addEventListener("touchend", stopDragging);
  window.addEventListener("touchmove", drag);

  let isDragging = false;

  function startDragging(e) {
    e.preventDefault();
    isDragging = true;
  }

  function stopDragging() {
    isDragging = false;
  }

  function drag(e) {
    if (!isDragging) return;

    // 計算滑桿的新位置
    var pos = getCursorPos(e, container);
    if (pos < 0) pos = 0;
    if (pos > containerWidth) pos = containerWidth;

    // 更新滑桿和上層圖片裁剪區域
    slider.style.left = pos + "px";
    overlay.style.clipPath = `inset(0 ${containerWidth - pos}px 0 0)`;
  }

  function getCursorPos(e, container) {
    var rect = container.getBoundingClientRect();
    var x = e.touches ? e.touches[0].pageX : e.pageX;
    return x - rect.left;
  }
}

// 初始化比較功能
document.addEventListener("DOMContentLoaded", initComparisons);
</script>

<p style="text-align: center;"><em>Fg.5 兩場景PATH MAP比較 </em></p>

### 人流密度分布圖 Density Map 

![image_example](/images/NeuroFlow/FDM2.png)

<p style="text-align: center;"><em>Fg.6 原本環境，Density MAP</em></p>

![image_example](/images/NeuroFlow/FDM1.png)

<p style="text-align: center;"><em>Fg.7 置入裝置後，Density MAP</em></p>

## 未來發展 Vision

目前程式已將基礎架構完成，接下來將整合LLM、VLM等AI進入Agent。以下為幾個主要的目標整合方向。1. Agent、行程設置。從社群媒體上爬文，透過LLM分析該用戶的個性，生成一套可能的於奇美博物館內的行程，包含其性格、垂直動線偏好、移動速度等。此部分取代過往透過官方數據，或專門的參數機率設置模型等，可針對特定人、族群，生成任務。2. 模擬過程中之決策行為。目前程式透過if-else模擬決策行為，當agent想去特定空間，但不曉得該空間的位置時，會嘗試透過wander模式找尋，並且考慮前往資訊節點（Info_node）設法取得目的地資訊。未來應可透過LLM的反思、記憶（(Park, J. S., et al., 2023)）等方式進行更近似於真實人類的判斷。

## 參考資料 Reference


[Izaki, Å., Uyar, G., & Jones, S. (2022). *Flow: Agent Simulation Framework with Spatial Choice for Multilevel Buildings*. ](https://www.researchgate.net/publication/363838891_Flow_Agent_Simulation_Framework_with_Spatial_Choice_for_Multilevel_Buildings)

[Uyar, G., Izaki, Å., Anklesaria, F., & Spencer, R. (2022). *Applying Flow simulation framework to model passenger behaviour in an airport terminal in North America*. ](https://www.researchgate.net/publication/363839131_Applying_Flow_simulation_framework_to_model_passenger_behaviour_in_an_airport_terminal_in_North_America)

[Park, J. S., O’Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). *Generative Agents: Interactive Simulacra of Human Behavior*.](http://arxiv.org/abs/2304.03442)

[Schaumann, D., Morad, M., Zinger, E., Putievsky Pilosof, N., Sopher, H., Brodeschi, M., … Kalay, Y. (2016). *A computational framework to simulate human spatial behavior in built environments*. ](https://www.researchgate.net/publication/303973571_A_computational_framework_to_simulate_human_spatial_behavior_in_built_environments)
