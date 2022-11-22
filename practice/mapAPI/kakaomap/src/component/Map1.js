/* global kakao */
import React, { useEffect } from "react";
import { Dialog } from '@mui/material';
import Slide from '@mui/material/Slide';
// import cn from "classnames";
// import "../styles/Map.scss";

const { kakao } = window;
const Transition = React.forwardRef(function Transition(props, ref) {
  return <Slide direction="up" ref={ref} {...props} />;
});

const Map1 = () => {
  const [open, setOpen] = React.useState(false);

  const ref = React.useRef();
 
  const handleClose = () => {
    setOpen(false);
  }

  const handleOpenKaKao = () => {
    setOpen(true);
  }

  useEffect(() => {
    const st = setTimeout(() => {
      if (open) {
        let container = document.getElementById("map");
        // let container = ref.current;
        console.log(container)
        let options = {
          center: new kakao.maps.LatLng(37.566826, 126.9786567),
          level: 3,
        };
        let map = new kakao.maps.Map(container, options);
      }
    }, 200)
  }, [open])

  return (
    <>
      <button onClick={handleOpenKaKao}>모달창 열려라!!</button>
      <Dialog open={open} onClose={handleClose} fullScreen TransitionComponent={Transition}>
        {/* <div style={{ margin: "50px"}}> */}
        <button onClick={handleClose}> 닫기 </button>
          <div id="map" style={{ width: "100%", height: "100%"}}>
          </div>
        {/* </div> */}
      </Dialog>
    </>
  );
};

export default Map1;